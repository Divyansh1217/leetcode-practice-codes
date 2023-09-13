# Write your MySQL query statement belowS
SELECT Customer.name
FROM Customer
WHERE NOT (Customer.referee_id)=2 OR (Customer.referee_id) IS NULL ;
