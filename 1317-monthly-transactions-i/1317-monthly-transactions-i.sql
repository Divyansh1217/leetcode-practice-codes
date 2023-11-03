# Write your MySQL query statement below
select DATE_FORMAT(trans_date, "%Y-%m") as month, country, count(state) as trans_count, count(case when state='approved' then state end) as approved_count, sum(amount) as trans_total_amount, IFNULL(sum(case when state='approved' then amount end),0) as approved_total_amount
from Transactions
group by Year(trans_date),Month(trans_date),country;