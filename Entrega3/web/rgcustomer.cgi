#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>RgC</title>')
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
      <h1>Register A New Customer</h1>
      <p>{}</p>
      <form method="post" action="rgcustomer.cgi">
          <label for="cust_no">Customer Number:</label>
          <input type="number" name="cust_no" id="cust_no" step="1" required><br><br>

          <label for="name">Name:</label>
          <input type="text" name="name" id="name" required><br><br>

          <label for="email">E-Mail:</label>
          <input type="text" name="email" id="email" required><br><br>

          <label for="phone">Phone Number:</label>
          <input type="text" name="phone" id="phone"><br><br>

          <label for="address">Address:</label>
          <input type="text" name="address" id="address"><br><br>

          <input type="submit" value="Add Customer" class="green-button">
      </form>
      <form method="get" action="main.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>
  '''

  # Process form submission
  if "cust_no" in form and "name" in form and "email" in form:
    cust_no = form["cust_no"].value
    name = form["name"].value
    email = form["email"].value
    phone = form["phone"].value if "phone" in form else None
    address = form["address"].value if "address" in form else None

    try:
      # Insert new product into the database
      sql = 'INSERT INTO customer (cust_no, name, email, phone, address) VALUES (%(cust_no)s, %(name)s, %(email)s, %(phone)s, %(address)s);'
      data = {'cust_no': cust_no, 'name': name, 'email': email, 'phone': phone, 'address': address}
      cursor.execute(sql, data)
      connection.commit()
      message = "Customer added successfully!"
    except (Exception, psycopg2.Error) as error:
      connection.rollback()
      message = f"Error adding customer: {str(error)}"
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