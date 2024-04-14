import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='2210')

cur=mydb.cursor()

cur.execute("CREATE DATABASE rashmi")
