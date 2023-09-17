# Write your MySQL query statement below
SELECT s1.score ,COUNT(s2.score) as 'rank'
FROM Scores s1,(SELECT DISTINCT score FROM Scores) s2
WHERE s2.score>=s1.Score
GROUP BY s1.Id
ORDER BY s1.score DESC;