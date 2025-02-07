create database if not exists instagramdb;
use instagramdb;

create table if not exists users(
userid int primary key,
username varchar(50),
email varchar(50)
);

create table if not exists posts(
postid int primary key,
userid int,
caption varchar(50)
);
insert into users(userid,username,email)
values
(1,'Bimal','sharmabimal123@gmail.com'),
(2,'Hari','hariclark@gmail.com'),
(3,'Ravi','ravigautamxx.com');

insert into posts(postid,userid,caption)
values
(1,101,"light"),
(2,102,'air'),
(3,103,'water');

use instagramdb;
#To view all the tables we just made
show tables;

#To fetch all the values from a specified table
select * from users;
select * from posts;
