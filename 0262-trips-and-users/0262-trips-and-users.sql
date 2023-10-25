# Write your MySQL query statement below
sELECT _trips.Request_at AS 'Day', round(
    SUM(case _trips.Status WHEN 'cancelled_by_driver' THEN 1 
                      WHEN 'cancelled_by_client' THEN 1 
        ELSE 0 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips _trips
WHERE '2013-10-01' <= _trips.Request_at AND _trips.Request_at <= '2013-10-03' 

AND _trips.Client_Id IN (
    SELECT Users_Id 
    FROM Users _users 
    WHERE Banned = 'No') 
                         
AND _trips.Driver_Id IN (
    SELECT Users_Id 
    FROM Users _users 
    WHERE Banned = 'No') 
    
GROUP BY _trips.Request_at