create database company1;
use company1;
create table employee1(
empid int,
name varchar(20),
salary int,
depart varchar(20),
age int
);
insert into employee1(empid,name,salary,depart,age)
values
(1,'Bimal',14000,'IT',20),
(2,'Raman',12000,'HR',19),
(3,'raman',13000,'IT',27);

#where clause---!
select name 
from employee1
where salary>12000;

#Limit clause===>Restricts the number of Rows
select * 
from employee1
limit 1;

#order by clause
select * from employee1 order by salary asc;

#Mxximum salary among the all
select salary from employee1
order by salary desc
limit 1;