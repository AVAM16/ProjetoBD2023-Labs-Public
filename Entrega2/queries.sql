--1
SELECT customer.name FROM customer
    INNER JOIN places ON customer.cust_no = places.cust_no
    INNER JOIN eorder ON places.order_no = eorder.order_no
    INNER JOIN contains ON eorder.order_no = contains.order_no
    INNER JOIN product ON contains.sku = product.sku
WHERE EXTRACT(YEAR FROM eorder.date) = 2023
  AND contains.qty *  product.price > 50;

--2

(SELECT employee.name FROM employee
    INNER JOIN works ON employee.ssn = works.ssn
    INNER JOIN workplace ON works.address = workplace.address
    INNER JOIN warehouse ON workplace.address = warehouse.address
    INNER JOIN process ON employee.ssn = process.ssn
    INNER JOIN eorder ON process.order_no = eorder.order_no
WHERE EXTRACT(YEAR FROM eorder.date) = 2023
    AND EXTRACT(MONTH FROM eorder.date) = 1)
EXCEPT
(SELECT employee.name FROM employee
    INNER JOIN works ON employee.ssn = works.ssn
    INNER JOIN workplace on works.address = workplace.address
    INNER JOIN office on workplace.address = office.address);

--3
SELECT name FROM product
WHERE sku = 
(SELECT product.sku FROM product
    INNER JOIN contains on product.sku = contains.sku
    INNER JOIN eorder on eorder.order_no = contains.order_no
    INNER JOIN sale on eorder.order_no = sale.order_no
    GROUP BY product.sku
    HAVING SUM(contains.qty) >= ALL (
        SELECT SUM(contains.qty) FROM contains
        INNER JOIN product on product.sku = contains.sku
        INNER JOIN eorder on eorder.order_no = contains.order_no
        INNER JOIN sale on eorder.order_no = sale.order_no
        GROUP BY product.sku
        ));


--4

SELECT  SUM(qty * price) as value FROM sale
    INNER JOIN eorder on sale.order_no = eorder.order_no
    INNER JOIN contains on eorder.order_no = contains.order_no
    INNER JOIN product on product.sku = contains.sku
    GROUP BY sale.order_no;