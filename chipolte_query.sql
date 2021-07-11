

SELECT * 

FROM orders

WHERE item_name = "Steak Burrito";

SELECT choice_description, max(item_price), min(item_price), AVG(item_price)

FROM orders

WHERE item_name = "Steak Burrito"

GROUP BY choice_description;

SELECT * FROM orders;

SELECT item_name, sum(quantity) AS "number_sold"

FROM orders

GROUP BY item_name

ORDER BY number_sold DESC;


SELECT count(*) 

FROM orders

WHERE item_name LIKE "%Chips%";

SELECT * FROM orders;



SELECT DISTINCT item_name, quantity, item_price 

FROM orders

WHERE item_name LIKE "%Chips%Guac%";


SELECT * FROM orders;



