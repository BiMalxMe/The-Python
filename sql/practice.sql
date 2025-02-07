create database practice;

use practice;
create table p1(
name varchar(20),
age int, 
department varchar(20),
city varchar(20),
salary int
);

insert into p1(name,age,department,city,salary)
values
('Safal',13,'IT','Mumbai',9000),
('Samikshya',23,'DR','ktm',12000),
('Disha',21,'HR','Mumbai',25000),
('Saurav',19,'IT','sydney',20000);

select * from p1;


#Total number of employee in each city
select city,count(name) as counted from p1
group by city;

#waq to find the max salary of employee in each city in descending 
select city,max(salary) AS salmax
from p1
group by city
order by salmax desc;


#waq to display department names alonside the total count of employees in each department ,sorting 
#the results by the total numbers of employees in descending order


select department,count(name) as coutt
From p1
group by department
order by coutt desc;


#waq to list departments where the average salry is greater than 1200 aslso 
#display the departmnet name and average salary

select department,avg(salary) as avgsal
from p1
group by department
having avgsal>13000;


