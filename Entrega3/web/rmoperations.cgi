#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>RmO</title>')
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
      <h1>Remove Products, Suppliers, Customers</h1>
      <p>Removing Products, Suppliers, Customers  will affect other elements in the DataBase</p>
      <p>{}</p>
      <form method="post" action="rmoperations.cgi">
          <label for="sku">Product SKU:</label>
          <input type="text" id="sku" name="sku">
          <input type="submit" value="Remove Product" class="green-button">
      </form>

      <form method="post" action="rmoperations.cgi">
          <label for="tin">Supplier TIN:</label>
          <input type="text" id="tin" name="tin">
          <input type="submit" value="Remove Supplier" class="green-button">
      </form>

      <form method="post" action="rmoperations.cgi">
          <label for="cust_no">Customer Number:</label>
          <input type="text" id="cust_no" name="cust_no">
          <input type="submit" value="Remove Customer" class="green-button">
      </form>
      <form method="get" action="main.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>
  '''

  # Process form submission
  if "sku" in form and form.getvalue("sku"):
    product_sku = form.getvalue("sku")

    try:
        # Remove the product from the database
        cursor.execute("SET CONSTRAINTS ALL DEFERRED")
        sql = "DELETE FROM product WHERE SKU = %(sku)s"
        data = {"sku": product_sku}
        cursor.execute(sql, data)
        sql = "DELETE FROM orders WHERE order_no NOT IN (SELECT order_no FROM contains);"
        cursor.execute(sql)
        connection.commit()

        message = "Product removed successfully!"
    except (Exception, psycopg2.Error) as error:
        connection.rollback()
        message = f"Error removing product: {str(error)}"
  elif "tin" in form and form.getvalue("tin"):
    supplier_tin = form.getvalue("tin")

    try:
        # Remove the supplier from the database
        cursor.execute("SET CONSTRAINTS ALL DEFERRED")
        sql = "DELETE FROM supplier WHERE TIN = %(tin)s"
        data = {"tin": supplier_tin}
        cursor.execute(sql, data)
        connection.commit()

        message = "Supplier removed successfully!"
    except (Exception, psycopg2.Error) as error:
        connection.rollback()
        message = f"Error removing supplier: {str(error)}"
  elif "cust_no" in form and form.getvalue("cust_no"):
    customer_no = form.getvalue("cust_no")

    try:
        # Remove the customer from the database
        cursor.execute("SET CONSTRAINTS ALL DEFERRED")
        sql = "DELETE FROM customer WHERE cust_no = %(cust_no)s"
        data = {"cust_no": customer_no}
        cursor.execute(sql, data)
        connection.commit()

        message = "Customer removed successfully!"
    except (Exception, psycopg2.Error) as error:
        connection.rollback()
        message = f"Error removing customer: {str(error)}"
  else:
      message = ""

  # Display the HTML form
  print(html_template.format(message))
except Exception as e:
  print('<h1>An error occurred.</h1>') 
  print('<p>{}</p>'.format(e))
finally:
  if connection is not None:
    connection.close()
print('</body>')
print('</html>')