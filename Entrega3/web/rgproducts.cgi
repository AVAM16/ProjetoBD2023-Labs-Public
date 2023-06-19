#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>RgP</title>')
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
      <h1>Register A New Product</h1>
      <p>{}</p>
      <form method="post" action="rgproducts.cgi">
          <label for="sku">SKU:</label>
          <input type="text" name="sku" id="sku" required><br><br>

          <label for="name">Name:</label>
          <input type="text" name="name" id="name" required><br><br>

          <label for="description">Description:</label>
          <textarea name="description" id="description"></textarea><br><br>

          <label for="price">Price:</label>
          <input type="number" name="price" id="price" step="0.01" required><br><br>

          <label for="ean">EAN:</label>
          <input type="number" name="ean" id="ean"><br><br>

          <input type="submit" value="Add Product" class="green-button">
      </form>
      <form method="get" action="main.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>
  '''

  # Process form submission
  if "sku" in form and "name" in form and "price" in form:
    sku = form["sku"].value
    name = form["name"].value
    description = form["description"].value if "description" in form else None
    price = form["price"].value
    ean = form["ean"].value if "ean" in form else None

    try:
      # Insert new product into the database
      sql = 'INSERT INTO product (sku, name, description, price, ean) VALUES (%(sku)s, %(name)s, %(description)s, %(price)s, %(ean)s);'
      data = {'sku': sku, 'name': name, 'description': description, 'price': price, 'ean': ean}
      cursor.execute(sql, data)
      connection.commit()
      message = "Product added successfully!"
    except (Exception, psycopg2.Error) as error:
      connection.rollback()
      message = f"Error adding product: {str(error)}"
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