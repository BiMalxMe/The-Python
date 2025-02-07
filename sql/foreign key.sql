use school;
create table base(
id int primary key,
stname varchar(20)
);

create table child(
course varchar(20),
id int,
foreign key(id) references base(id) 
);



