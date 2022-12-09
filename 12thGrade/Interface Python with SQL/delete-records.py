import mysql.connector as conn

#this line not necessary if you give some fixed name like 'mydb' to database in line 6
db_name = input("Enter name of database: ")

db = conn.connect(host='localhost', user='root', password='root', database=db_name)

cursor = db.cursor()

#following lines not necessary if you give some fixed name like 'mytable', 'clm1' instead
table_name = input("Enter name of table: ")
clm_name = input("Enter name of respective column: ")

del_data = input("Enter value whose row is to be deleted: ")

cmd = "DELETE FROM {table} WHERE {clm} = {del_key}".format(table=table_name, clm=clm_name, del_key=del_data)

cursor.execute(cmd)
db.commit()

### Extra
display_cmd = "SELECT * FROM {table}".format(table=table_name)
cursor.execute(display_cmd)
data = cursor.fetchall()
print("The updated table is:")
for row in data:
    print(row)

db.close()
