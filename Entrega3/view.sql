--product_sales(sku, order_no, qty, total_price, year, month, day_of_month, day_of_week, city)
DROP VIEW IF EXISTS product_sales CASCADE;
CREATE VIEW product_sales AS
SELECT c.SKU, c.order_no, c.qty, (c.qty * p.price) AS total_price,
       DATE_PART('Year', o.date) AS year,
       DATE_PART('month', o.date) AS month,
       DATE_PART('day', o.date) AS day_of_month,
       DATE_PART('dow', o.date) AS day_of_week,
       substring(cust.address FROM '[0-9]{4}-[0-9]{3} (.+)$') AS city
FROM contains c
JOIN orders o ON c.order_no = o.order_no
JOIN pay py ON o.order_no = py.order_no
JOIN customer cust ON py.cust_no = cust.cust_no
JOIN product p ON c.SKU = p.SKU;
