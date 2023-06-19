#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>MkO</title>')
print('<link rel="stylesheet" type="text/css" href="style.css">')
print('</head>')
print('<body>')
print('<h1>Make an Order</h1>')
connection = None
try:
  connection = psycopg2.connect(login.credentials)
  connection.autocommit = False
  cursor = connection.cursor()
  sql = 'SELECT sku, name, price FROM product;'
  cursor.execute(sql)
  result = cursor.fetchall()
  num = len(result)
  # Displaying results
  column_names = ['SKU', 'Name', 'Price(euros)']
  print('<form action="mkorder2.cgi" method="get">')
  print('<table class="result-table">')
  print('<tr>') 
  for column in column_names:
    print('<th>{}</th>'.format(column))
  print('<th>Product Quantity</th>')
  print('</tr>')
  for row in result:
    print('<tr>')
    for value in row:
    # The string has the {}, the variables inside format() will replace the {}
      print('<td>{}</td>'.format(value))
    print('<td>')
    print('<input type="hidden" name="selected_products[]" value="{}">'.format(row[0]))
    print('<input type="number" name="quantity[]" min="0" max="9999" value="0">')
    print('</td>')
    print('</tr>')
  print('</table>')
  cursor.close()
  print('''
    <input type="submit" value="Order"  onclick="window.location.href='mkorder2.cgi'" class="green-button">
    <br>
    <input type="button" value="Go Back" onclick="window.location.href='main.cgi'" class="red-button">
    </form>''')
except Exception as e:
  print('<h1>An error occurred.</h1>') 
  print('<p>{}</p>'.format(e))
finally:
  if connection is not None:
    connection.close()
print('</body>')
print('</html>')