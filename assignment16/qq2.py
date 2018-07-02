#q2 Insert values in the tables.

import pymysql as py

db=py.connect("localhost","root","123","book")
cursor=db.cursor()
qr= 'insert into book values(1,23,"dfg","fee")'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr= 'insert into Titles values(1,"dfg",23,"fee",456)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()
qr= 'insert into Publishers values(1,"dfg","fee23",456,678)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()


qr= 'insert into Zipcodes values(1,"dfg","fee23",456)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr= 'insert into Authertitle values(1,23,456)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr= 'insert into Authers values(1,"abc","dfg","ser")'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

db.close