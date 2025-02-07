use ecom;

#find order details using procedure without params

 -- using it as new terminating symbol
Delimiter \
create procedure getallorder()
BEGIN
select * from cusstomer;
END\
Delimiter ;
--  changing into original form fir avoiing errors

call getallorder();


use del;
#find order details using procedure with params
Delimiter \
create procedure getallorder(in id int)
BEGIN
select * from tru where id=id;
END\
Delimiter ;
--  changing into original form fir avoiing errors

call getallorder(2);