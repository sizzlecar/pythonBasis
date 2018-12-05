import mysql.connector
# Python3 连接mysql

db = mysql.connector.connect(host="10.0.0.83",
                             user="root",
                             passwd="****",
                             database="hs_biz")
mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


