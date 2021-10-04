# Resto_list
 For creating DB Schemas
 ## WE have used draw.io as shown below
![](https://github.com/t007rushi/Resto_list/blob/main/Resto_list.drawio.png)
# Resto Owner table
![](https://github.com/t007rushi/Resto_list/blob/main/Profile_table.drawio.png)
<!-- ![](https://github.com/t007rushi/Resto_list/blob/main/script%20%20to%20retrive-fetch.txt) -->
-----------------Resto Owner (MAIN TABLE)-------------------

-----------Owner table
Profile_pic

  Name

  E-mail ID

  Phone Number

  Address


----------bank_detail table

  Bank Account Number

  Bank Name

  Branch Name

  IFSC Code

-------------------------------------------------------------

//render html file restaurant_owner_edit.html

-----------SQL Script

select * from owner_table as O join ban_detail B 
on O.id = B.b_acc_id
