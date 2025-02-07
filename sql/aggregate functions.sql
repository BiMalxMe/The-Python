use company1;
create table employee2(
empid int,
name varchar(20),
salary int,
depart varchar(20),
age int
);
insert into employee2(empid,name,salary,depart,age)
values
(1,'Bimal',14000,'IT',20),
(2,'Raman',12000,'HR',19),
(3,'raman',13000,'IT',27);

#agg function

#count
#sum
#avg
#min
#max

select count(name) from employee2;#IT counts the total number of name inputed,counts NOT NULL vals
select sum(age) from employee2;
select avg(salary) from employee2;
select min(salary) from employee2;
select max(salary) from employee2;


