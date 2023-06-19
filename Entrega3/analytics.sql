--query1 
SELECT city, year, month, day_of_month, day_of_week, SKU,
       SUM(qty) AS total_qty,
       SUM(total_price) AS total_value
FROM product_sales
WHERE year=2022
GROUP BY ROLLUP (city, month, day_of_month, day_of_week, SKU)
--ORDER BY city, year, month, day_of_month, day_of_week, SKU;

--query2 (tão simples!?)
SELECT month, day_of_week, AVG(total_price) AS daily_avg_value
FROM product_sales
WHERE year = 2022
GROUP BY month, day_of_week;