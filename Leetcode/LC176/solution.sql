SELECT Max(Salary) as SecondHighestSalary FROM Employee WHERE salary < (SELECT MAX(Salary) FROM Employee)