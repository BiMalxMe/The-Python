


use del;
create table tru(
name varchar(30),
id int ,
sclname varchar(20)
);

insert into tru(name,id,sclname)
values
('BImal',1,'Shining'),
('kumal',2,'Aroma'),
('Bibesh',3,'GopalJanak');

select * from tru;

#using truncate command
#-it removes values of the table but preserves the structure of the database


truncate table tru;
