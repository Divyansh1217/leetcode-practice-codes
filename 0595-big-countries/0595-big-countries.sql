# Write your MySQL query statement below
SELECT name,population,World.area
FROM World
WHERE area>=3000000 OR (population)>=25000000;