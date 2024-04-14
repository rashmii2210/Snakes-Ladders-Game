import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='your password')

cur=mydb.cursor()

cur.execute("CREATE DATABASE rashmi")
