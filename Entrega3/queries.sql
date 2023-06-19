--query1
SELECT DISTINCT c.cust_no, c.name
FROM customer c
JOIN pay p ON c.cust_no=p.cust_no
join orders o ON p.order_no=o.order_no
join contains cont ON o.order_no= cont.order_no
join product prod on cont.sku = prod.sku
GROUP BY c.cust_no, c.name
HAVING sum(prod.price*cont.qty)=(
    select SUM(prod.price*cont.qty)
    from customer c
    join pay p on c.cust_no=p.cust_no
    join orders o on p.order_no=o.order_no
    join contains cont on o.order_no=cont.order_no
    join product prod on cont.sku=prod.sku
    group by c.cust_no
    order by SUM(prod.price*cont.qty)
    LIMIT 1
    --subquery serve para encontrar o valor mais alto
    );

--query2
select DISTINCT e.name
from employee e
where not exists(
    select o.date
    from orders o
    where o.date <='2022-12-31' and o.date>='2022-01-01'
    EXCEPT
    Select o.date
    from process p
    join orders o on p.order_no =o.order_no
    WHERE p.ssn=e.ssn

);

--query3
SELECT EXTRACT(MONTH FROM o.date) AS month, COUNT(*) AS order_count
FROM orders o
LEFT JOIN pay p ON o.order_no = p.order_no
WHERE o.date >= '2022-01-01' AND o.date <= '2022-12-31' AND p.order_no IS NULL
GROUP BY EXTRACT(MONTH FROM o.date)
ORDER BY EXTRACT(MONTH FROM o.date);








--query para procurar por índice 7.1
SELECT order_no
FROM orders
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

--query para procurar por índice 7.2
SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

