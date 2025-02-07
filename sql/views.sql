create database _view; 
use _view;
create table vv(
id int,
name varchar(20),
pass varchar(20)
);
insert into vv(id,name,pass)
values
(1,"KARAN",'956jyj44'),
(2,"SOMPAL",'ee773h'),
(3,"SANDY",'ee93kfmf');

create view secured as  #making password secure as it cant be viewd while viweing main table
select name,id
from vv;

select * from secured;