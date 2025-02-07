create database xyz;
use xyz;

create table employee(
id int primary key,
name varchar(20),
age int,
department varchar(20),
city varchar(50),
salary int
);

insert into employee(id,name,age,department,city,salary)
values
(1,'rahul',25,'IT','Pune',1500),
(2,'afsara',25,'HR','Mumbai',2500),
(3,'abhimanyu',25,'IT','Mumbai',3500),
(4,'aditya',25,'IT','Chandigarh',4500),
(5,'raj',25,'IT','Indore',5500);

#WAQ to change salary to 50000 of HR department


#to disable the safe mode
SET SQL_SAFE_UPDATES=0;


update employee
set salary=50000
where department='HR';
select * from employee;

#WAQ to change the emolyee name from raj to raaj

update employee
set name='raaj'
where name='raj' 