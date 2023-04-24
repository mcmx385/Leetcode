SELECT distinct l1.num as ConsecutiveNums from logs l1, logs l2, logs l3 where l1.id=l2.id-1 and l2.id=l3.id-1 and l1.num=l2.num and l2.num=l3.num

SELECT DISTINCT num AS ConsecutiveNums FROM Logs WHERE (Id+1,num) in (SELECT * FROM Logs) AND (Id+2,num) in (SELECT * FROM Logs)