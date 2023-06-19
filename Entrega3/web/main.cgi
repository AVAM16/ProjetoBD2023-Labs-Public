#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Menu</title>')
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
      <h1>Main Page</h1>
      <p>Welcome to the main page of the G22 DataBase!</p>
      <form method="get" action="rgproducts.cgi">
          <input type="submit" value="Register a new Product" class ="green-button big-button">
      </form>
      <form method="get" action="rgsupplier.cgi">
          <input type="submit" value="Register a new Supplier" class="green-button big-button">
      </form>
      <form method="get" action="upproducts.cgi">
          <input type="submit" value="Update an existing Product" class="yellow-button big-button">
      </form>
      <form method="get" action="rgcustomer.cgi">
          <input type="submit" value="Register a new Customer" class="green-button big-button">
      </form>
      <form method="get" action="rmoperations.cgi">
          <input type="submit" value="Remove Products, Suppliers, Customers" class="yellow-button big-button">
      </form>
      <form method="get" action="mkorder.cgi">
          <input type="submit" value="Make an Order" class="green-button big-button">
      </form>
      <form method="get" action="payorder.cgi">
          <input type="submit" value="Pay an Order" class="green-button big-button">
      </form>
  '''
  print(html_template)
except Exception as e:
  print('<h1>An error occurred.</h1>') 
  print('<p>{}</p>'.format(e))
finally:
  if connection is not None:
    connection.close()
print('</body>')
print('</html>')