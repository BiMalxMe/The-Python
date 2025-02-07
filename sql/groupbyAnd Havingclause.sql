use company1;
#Group By clause--only use aggeregate func to run
select depart,avg(salary) as avgsal from employee2
group by depart;

#having clause--gives conditions on group by and aggregate funcs

select depart,avg(salary) as avgsal from employee2
group by depart
having avgsal>20;			#only new created columns will be used after having clause
