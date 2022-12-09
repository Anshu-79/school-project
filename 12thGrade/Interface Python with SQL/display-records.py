import mysql.connector as conn

#this line not necessary if you give some name like 'mydb' to database in line 6
db_name = input("Enter name of database: ")

db = conn.connect(host='localhost', user='root', password='root', database=db_name)

cursor = db.cursor()

table_name = input("Enter name of table: ")

cmd = "SELECT * FROM {table}".format(table=table_name)

cursor.execute(cmd)
data = cursor.fetchall()

for row in data:
    print(row)