#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>UpP</title>')
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
      <h1>Update An Existing Product</h1>
      <p>{}</p>
      <form method="post" action="upproducts.cgi">
          <label for="sku">SKU:</label>
          <input type="text" name="sku" id="sku" required><br><br>

          <label for="description">Description:</label>
          <textarea name="description" id="description"></textarea><br><br>

          <label for="price">Price:</label>
          <input type="number" name="price" id="price" step="0.01"><br><br>

          <input type="submit" value="Update Product" class="green-button">
      </form>
      <form method="get" action="main.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>
  '''

  # Process form submission
  if "sku" in form:
    sku = form["sku"].value
    description = form["description"].value if "description" in form else None
    price = form["price"].value if "price" in form else None
    try:
      # Insert new product into the database
      if description is not None:
        sql = 'UPDATE product SET description = %(description)s WHERE sku = %(sku)s;'
        data = {'sku': sku, 'description': description}
        cursor.execute(sql, data)
      if price is not None:
        sql = 'UPDATE product SET price = %(price)s WHERE sku = %(sku)s;'
        data = {'sku': sku, 'price': price}
        cursor.execute(sql, data)
      connection.commit()
      if description is not None or price is not None:
        message = "Product updated successfully!"
      else:
        message = "Need something to update!"
    except (Exception, psycopg2.Error) as error:
      connection.rollback()
      message = f"Error updating product: {str(error)}"
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