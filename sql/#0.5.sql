create database college;
use college;
CREATE TABLE courses (
    PersonID int,
    course varchar(255)
);
insert into courses(PersonID,course)
values (1,'Maths');


#To view the inputed data,
select * from courses;

#to view all the table from the database
show tables;