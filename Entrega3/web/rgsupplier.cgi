#!/usr/bin/python3
import psycopg2, cgi
import login
from datetime import datetime
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>RgS</title>')
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
      <h1>Register A New Supplier</h1>
      <p>{}</p>
      <form method="post" action="rgsupplier.cgi">
          <label for="tin">TIN:</label>
          <input type="text" name="tin" id="tin" required><br><br>

          <label for="name">Name:</label>
          <input type="text" name="name" id="name"><br><br>

          <label for="address">Address:</label>
          <input type="text" name="address" id="address"><br><br>

          <label for="sku">SKU:</label>
          <input type="text" name="sku" id="sku" required><br><br>

          <label for="date">Date:</label>
          <input type="date" name="date" id="date"><br><br>

          <input type="submit" value="Add Supplier" class="green-button">
      </form>
      <form method="get" action="main.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>
  '''

  # Process form submission
  if "tin" in form and "sku" in form:
    tin = form["tin"].value
    name = form["name"].value if "name" in form else None
    address = form["address"].value if "address" in form else None
    sku = form["sku"].value
    date = form["date"].value if "date" in form else None

    try:
      # Insert new product into the database
      date = datetime.strptime(date, '%Y-%m-%d').date()
      sql = 'INSERT INTO supplier (tin, name, address, sku, date) VALUES (%(tin)s, %(name)s, %(address)s, %(sku)s, %(date)s);'
      data = {'tin': tin, 'name': name, 'address': address, 'sku': sku, 'date': date}
      cursor.execute(sql, data)
      connection.commit()
      message = "Supplier added successfully!"
    except (Exception, psycopg2.Error) as error:
      connection.rollback()
      message = f"Error adding supplier: {str(error)}"
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