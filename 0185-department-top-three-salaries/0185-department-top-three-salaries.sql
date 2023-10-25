# Write your MySQL query statement below
select d.name as Department,e.name as Employee,(e.salary) as Salary
from (select name,departmentId,salary,dense_rank() over (partition by departmentId order by salary desc) as also from employee) e
LEft Join Department d on(d.id=e.departmentId)
where also<=3;
