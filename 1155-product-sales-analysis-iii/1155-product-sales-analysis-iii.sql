/* Write your T-SQL query statement below */

SELECT p.product_id, S.year as first_year, S.quantity, S.price
FROM product p
left join Sales S on p.product_id=S.product_id
WHERE (S.product_id,S.year) in (select S1.product_id,min(S1.year) from Sales S1 group by S1.product_id)