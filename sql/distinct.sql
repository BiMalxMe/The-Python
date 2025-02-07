create database company;
use company;
create table employee(
empid int,
name varchar(20),
salary int
);
insert into employee(empid,name,salary)
values
(1,'Bimal',14000),
(2,'Raman',12000),
(3,'raman',13000);
 
 select * from employee;
 
 #selecting ditinct values from a single colum
 select distinct name
 from employee;
 
 
 #selecting ditinct values from a multiple column
 select distinct name,empid
 from employee;