#!/usr/bin/python3
from datetime import datetime
import decimal
import psycopg2, cgi
import login
form = cgi.FieldStorage()
selected_products = form.getlist('selected_products[]')
quantities = form.getlist('quantity[]')
product_quantities = zip(selected_products, quantities)
products_to_order = [(product, quantity) for product, quantity in product_quantities if int(quantity) > 0]
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>MkO</title>')
print('</head>')
print('<body>')
connection = None
try:
  connection = psycopg2.connect(login.credentials)
  connection.autocommit = False
  cursor = connection.cursor()
  html_template = '''
  <!DOCTYPE html>
  <html>    
  <head>
      <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
      <h1>Make an Order: Price {}</h1>
      <p>{}</p>
      <form method="post" action="mkorder2.cgi">
          <label for="order_no">Order Number:</label>
          <input type="text" name="order_no" id="order_no" required><br><br>

          <label for="cust_no">Customer Number:</label>
          <input type="text" name="cust_no" id="cust_no" required><br><br>
          
          <label for="date">Date:</label>
          <input type="date" name="date" id="date" required><br><br>

          <!-- Hidden input fields to store the selected products and quantities -->
          {}

          <input type="submit" value="Make the Order" class="green-button">
      </form>
      <form method="get" action="mkorder.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>
  '''

  # Process form submission
  if "order_no" in form and "cust_no" in form and "date" in form:
    order_no = form["order_no"].value
    cust_no = form["cust_no"].value
    date = form["date"].value

    try:
      # Insert new product into the database
      date = datetime.strptime(date, '%Y-%m-%d').date()
      cursor.execute("SET CONSTRAINTS ALL DEFERRED;")
      sql = 'INSERT INTO orders (order_no, cust_no, date) VALUES (%(order_no)s, %(cust_no)s, %(date)s);'
      data = {'order_no': order_no, 'cust_no': cust_no, 'date': date}
      cursor.execute(sql, data)
      for sku, quantity in products_to_order:
        sql = 'INSERT INTO contains (order_no, SKU, qty) VALUES (%(order_no)s, %(sku)s, %(qty)s);'
        data = {'order_no': order_no, 'sku': sku, 'qty': quantity}
        cursor.execute(sql, data)
      connection.commit()
      message = "Order made successfully!"
    except (Exception, psycopg2.Error) as error:
      connection.rollback()
      message = f"Error making Order: {str(error)}"
  else:
    message = ""

  hidden_fields = ""
  for product, quantity in products_to_order:
    hidden_fields += '<input type="hidden" name="selected_products[]" value="{}">'.format(product)
    hidden_fields += '<input type="hidden" name="quantity[]" value="{}">'.format(quantity)

  price = 0
  for sku, quantity in products_to_order:
    try:
      sql = 'SELECT price FROM product WHERE SKU = %s;'
      data = (sku,)
      cursor.execute(sql, data)
      price_product = cursor.fetchone()[0]
      price_product = decimal.Decimal(price_product)
      quantity = int(quantity)
      price += price_product * quantity
    except (Exception, psycopg2.Error) as error:
      connection.rollback()
      message = f"Error getting product price: {str(error)}"
      break
  # Display the HTML form
  print(html_template.format(price, message, hidden_fields))
except Exception as e:
  print('<h1>An error occurred.</h1>') 
  print('<p>{}</p>'.format(e))
finally:
  if connection is not None:
    connection.close()
print('</body>')
print('</html>')