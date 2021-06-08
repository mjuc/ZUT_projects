import mysql.connector

con=mysql.connector.connect(user='user',password='',host='127.0.0.1',database="lab")

crs=con.cursor()
crs.execute("SELECT * FROM test WHERE type='unit'")
result=crs.fetchall()
print(result)
con.close()