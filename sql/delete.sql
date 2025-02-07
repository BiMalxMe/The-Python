create database del;
use del;

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



#WAQ to delete all the records from the table  of the department HR

delete from employee
where department='HR';
select * from employee;

#WAQ to delete all the records from the table  of the name raaj
delete from employee
where name='raj';