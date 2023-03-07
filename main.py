import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abhi@131',
    port='3306',
    database='rrr'
    )
print("connected db")
gbdata=db.cursor()
gbdata.execute("select * from rr")
h=gbdata.fetchall()
for rr in h:
    print(rr)
gbdata.close()
print("disconnect successfully")



