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


#adding new column and setting default value to Java
alter table employee
add skill varchar(20) default 'Java';

select * from employee;


#Dropping a column
alter table employee
drop column skill;


#modify the existing datatype of a table
alter table employee
modify column salary varchar(20);


#changing the name of the column
alter table employee
change city home varchar(20);#change oldcolName newcolName data type


#Rename command
alter table employee
rename column home to city;

