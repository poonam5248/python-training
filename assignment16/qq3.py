#q3  Update any values in any of the tables. Print the original and updated values.

import pymysql as py

db=py.connect("localhost","root","123","book")
cursor=db.cursor()

qr= 'update book set book_id=4 where title_id= 23'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr='select * from book'
cursor.execute(qr)
result=cursor.fetchall()
for r in result:
    print(r)