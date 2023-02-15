import mysql.connector

db_local=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kishore@2000",
    database="local"
)
local_cursor=db_local.cursor()
# local_cursor.execute("Insert Into user values(%s,%s,%s,%s,%s)",(1,"adam","adam@abc.com",123460,"burnswick"))
# local_cursor.execute("Insert Into user values(%s,%s,%s,%s,%s)",(2,"joe","joe@abc.com",123478,"spring gardeb"))
# local_cursor.execute("Insert Into user values(%s,%s,%s,%s,%s)",(3,"josh","josh@abc.com",123478,"clayton park"))
# local_cursor.execute("Insert Into user values(%s,%s,%s,%s,%s)",(0,"mika","mika@abc.com",123543,"windsor street"))
# db_local.commit()
local_cursor.execute("select * from user")
for x in local_cursor:
     print(x)
# mycursor.execute("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))")



db_remote=mysql.connector.connect(
    host="35.224.170.125",
    user="root",
    passwd="",
    database="Ecommerce"
)
remote_cursor=db_remote.cursor()
    # remote_cursor.execute("Insert Into Inventory values(%s,%s,%s)",(3,"grape",60))
    # remote_cursor.execute("Insert Into Inventory values(%s,%s,%s)",(4,"pear",80))
    # remote_cursor.execute("DELETE FROM Inventory WHERE item_id=3")
    # db_remote.commit()
print("remote inventory")
remote_cursor.execute("select * from Inventory")
for x in remote_cursor:
    print(x)
print("order item now")
userIdForOrder=int(input("user id:"))
IdForOrder=input("item id:")
nameForOrder=input("item name:")
quantityForOrder=int(input("item quantity:"))
DateForOrder=input("date:")
remote_cursor.execute("select * from Inventory where item_id={}".format(IdForOrder))
product_quantitiy=0
for x in remote_cursor:
    product_quantitiy=x[2]
    
if quantityForOrder<=product_quantitiy:
    local_cursor.execute("Insert Into order_info values(%s,%s,%s,%s,%s)",(0,userIdForOrder,nameForOrder,quantityForOrder,DateForOrder))
    remote_cursor.execute("Update Inventory set available_quanity={} where item_id={}".format(product_quantitiy-quantityForOrder,IdForOrder))
else:
    print("order unsecessfull")
print("order_info")
local_cursor.execute("select * from order_info")
for x in local_cursor:
    print(x)
print("remote inventory")
remote_cursor.execute("select * from Inventory")
for x in remote_cursor:
    print(x)
#print(remote_cursor.execute("select * from Inventory where item_id={}".format(IdForOrder)))