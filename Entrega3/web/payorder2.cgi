#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
cust_no = form.getvalue('cust_no')
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>PayO</title>')
print('<link rel="stylesheet" type="text/css" href="style.css">')
print('</head>')
print('<body>')
print('<h1>Pay an Order: Customer {}</h1>'.format(cust_no))
connection = None
try:
  connection = psycopg2.connect(login.credentials)
  connection.autocommit = False
  cursor = connection.cursor()
  if 'order_no' in form:
      try:
        order_no = form.getvalue('order_no')
        order_no = int(order_no)

        # Inserting into the pay table
        sql_insert = "INSERT INTO pay (order_no, cust_no) VALUES (%(order_no)s, %(cust_no)s)"
        data_insert = {'order_no': order_no, 'cust_no': cust_no}
        cursor.execute(sql_insert, data_insert)
        connection.commit()
        print('<h2>Payment for Order {} has been successfully paid.</h2>'.format(order_no))
      except (Exception, psycopg2.Error) as error:
        connection.rollback()
        print('<h2>Payment for Order {} has not been paid.</h2>'.format(order_no))
  else:
    print('<h2>Orders to be paid:</h2>')
  sql = '''
    (SELECT orders.order_no, SUM(contains.qty*product.price) AS value
    FROM orders
    INNER JOIN contains ON orders.order_no = contains.order_no
    INNER JOIN product ON product.sku = contains.sku
    WHERE orders.cust_no = %(cust_no)s
    GROUP BY orders.order_no)
    EXCEPT
    (SELECT orders.order_no, SUM(contains.qty*product.price) AS value
    FROM orders
    INNER JOIN pay ON orders.order_no = pay.order_no
    INNER JOIN contains ON orders.order_no = contains.order_no
    INNER JOIN product ON product.sku = contains.sku
    WHERE orders.cust_no = %(cust_no)s
    GROUP BY orders.order_no)
  '''
  data = {'cust_no': cust_no, 'cust_no': cust_no}
  cursor.execute(sql, data)
  result = cursor.fetchall()
  num = len(result)
  # Displaying results
  column_names = ['Order Number', 'Price(euros)']
  print('<table class="result-table">')
  print('<tr>') 
  for column in column_names:
    print('<th>{}</th>'.format(column))
  print('<th>Pay</th>')
  print('</tr>')
  for row in result:
    print('<tr>')
    for value in row:
    # The string has the {}, the variables inside format() will replace the {}
      print('<td>{}</td>'.format(value))
    print('<td>')
    print('<form action="payorder2.cgi" method="get">')  # Move the form tag here
    print('<input type="hidden" name="order_no" value="{}">'.format(row[0]))
    print('<input type="hidden" name="cust_no" value="{}">'.format(cust_no))  # Add this line
    print('<input type="submit" value="Pay">')
    print('</form>')
    print('</td>')
    print('</tr>')
  print('</table>')
  cursor.close()
  print('<form action="payorder.cgi" method="get">')
  print('<input type="hidden" name="cust_no" value="{}">'.format(cust_no))  # Add this line
  print('<input type="button" value="Go Back" onclick="window.location.href=\'payorder.cgi\'" class="red-button">')
  print('</form>')
except Exception as e:
  print('<h1>An error occurred.</h1>') 
  print('<p>{}</p>'.format(e))
finally:
  if connection is not None:
    connection.close()
print('</body>')
print('</html>')