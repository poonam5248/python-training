import pymysql as py

db=py.connect("localhost","root","123","book")
cursor=db.cursor()
# qr= 'insert into book values("rsaggarw",12345,"a","b"),("Rpsin",13456,"a","v")'

qr='create table book(book_id int,title_id int,location char(20),genre char(20))'
cursor.execute(qr)
qr='create table Titles(title_id int,title char(10),ISBN int,publisher char(20),publisher_id int)'
cursor.execute(qr)
qr='create table Publishers(publisher_id int, name char(20),streetadd varchar(20),suite_num int,zipcode_id int)'
cursor.execute(qr)
qr='create table Zipcodes(zipcode_id int,city char(20),state char(20),zipcode int)'
cursor.execute(qr)
qr='create table Authertitle(auther_title_id int,auther_id int,title_id int)'
cursor.execute(qr)
qr='create table Authers(auther_id int,first_name char(20),middle_name char(20),last_name char(20))'
cursor.execute(qr)
# try:
#     cursor.execute(qr)
#     db.commit()
# except:
#     db.rollback()
db.close()