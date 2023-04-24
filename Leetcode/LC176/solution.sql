SELECT Max(Salary) as SecondHighestSalary FROM Employee WHERE salary < (SELECT MAX(Salary) FROM Employee)
SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1
SELECT IFNULL((SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
SELECT Salary FROM (SELECT Salary, dense_rank() OVER (ORDER BY Salary DESC) AS rank FROM Employee) AS t WHERE rank = 2