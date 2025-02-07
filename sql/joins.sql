create database ecom;
use ecom;

create table customer(
id int,
name varchar(50)
);
insert into customer(id,name)
values
(101,'Bimal'),
(102,'Safal'),
(103,'Binit'),
(104,'Sourav'),
(105,'Tisha');

use ecom;

create table orders(
id int primary key,
orders varchar(20)
);

insert into orders(id,orders)
values
(101,'Fruit'),
(103,'Ball'),
(105,'Utensils');


select * from customer;
select * from orders;


#--Inner join on the basis of id-------------------------------------------------------------------------------

#selecting all the common vals
select * 
from customer
inner join orders
on customer.id=orders.id;#took the common id names from those two tables
#selecting only id name and orders
select name,orders,customer.id 
from customer
inner join orders
on customer.id=orders.id;


#--left outer join on the basis of id-------------------------------------------------------------------------------


select * 
from customer
left outer join orders
On customer.id=orders.id;
#it basically gives all the values of the left side along with the common values (id) and common is not there 
#it baiscallly prints null value


#--right outer join on the basis of id-------------------------------------------------------------------------------


select * 
from customer
right join orders#we also can write only rightjoin
On customer.id=orders.id;
#it basically gives all the values of the right side along with the common values (id)'s rows and common is not there 
#it baiscallly prints null value



#--full join on the basis of id-------------------------------------------------------------------------------
#we use union for full join in Mysql
#we do Lf UNION RJ

select * 
from customer
left outer join orders
On customer.id=orders.id
UNION
select * 
from customer
right join orders
On customer.id=orders.id;


#--cross join --------------------------------------------------------------------------------------------
#it bascally gives (m*n) values as m is table1 rows and n is table2 rows

select 	*
from customer
cross join orders;		#like cartesian prod



#making tables to demonstrate JOIN(i.e self join)
create table student(
sid int,
name varchar(20),
mentor_id int
);
insert into student(sid,name,mentor_id)
values
(1,'Riti',NULL),
(2,'Barris',1),
(3,'Sam',1),
(4,'Joshua',3);

#--self join----------------------------------------------------------------------------------------------------
#its CROSS PROD + CONDITION
select t1.name as mentor_id,t2.name as student_name
from student as t1
join student as t2
on t1.sid=t2.mentor_id;

#if you dont understand
#link:https://www.youtube.com/watch?v=RQPpP2ywA9k&t=3820s on 4:05:00


#left exclusive join---------------------------------------------------------------------------------------------
#first we do left join and ...............  .

select *
from  customer
left join orders
on customer.id=orders.id
where orders.id is Null;#print only the col vals which is null




