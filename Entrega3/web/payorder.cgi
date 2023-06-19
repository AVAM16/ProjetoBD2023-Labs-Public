#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>PayO</title>')
print('<link rel="stylesheet" type="text/css" href="style.css">')
print('</head>')
print('<body>')
print('<h1>Pay an Order</h1>')
print('<form action="payorder2.cgi" method="post">')  # Specify the action and method for the form
print('Enter your Customer Number: <input type="number" name="cust_no" required>')  # Add the input box with type "number"
print('<input type="submit" value="Submit" onclick="window.location.href=payorder2.cgi" class="green-button">')  # Add the submit button
print('</form>')
print('''<form method="get" action="main.cgi">
        <input type="submit" value="Go Back" class="red-button">
      </form>''')
print('</body>')
print('</html>')