use ecom;
select *  from customer;
select * from orders;


#selecting dupicates values of id from those two table--

#using UNION

select id
from customer
union
select id 
from orders;		#ids are not repeates

#Using UNION ALL

select id
from customer
union all
select id 
from orders;	