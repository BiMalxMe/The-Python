use company1;
select * from employee;
-- ------------------------ -------------------SUBQUERIES BY WHERE CLAUSE------------------------------------------------------------
# Q1. To find the minimum salary
# Q2. To find all employees having salary greater than min salary

# 1.
select min(salary) from employee;

#2.
select name,salary
from employee
where salary>(select min(salary) from employee);

use company1;
select * from employee1;

-- 1.Find the min age
select min(age) from employee1;

--  2 FInd the employee having min age
select name,age
from employee1
where age=(select min(age) from employee1);

-- ------------------------ -------------------SUBQUERIES BY FROM CLAUSE------------------------------------------------------------

-- Q1.Find the min age
select min(age) As min_age from employee1;

# Q2. To find all employees having age greater than min age
select name,age 
from employee1,(select min(age)as mage from employee1) as sq
where age>sq.mage;

-- ------------------------ -------------------SUBQUERIES BY SELECT CLAUSE------------------------------------------------------------
-- Q1. Find the avg age
select avg(age) from employee1;

-- Q1. Find the age and avg age
select age,(select avg(age) from employee1) as average
from employee1;



#select the nth highest salary
select distinct salary
from employee1
order by salary desc
limit 2,1;
