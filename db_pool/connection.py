from mysql import connector

connect= connector.connect(
    user= 'root',
    password='Nani@123',
    host='localhost',
    database= 'managment_db'
)

cursor=connect.cursor()