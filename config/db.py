import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Note@123",
    database="Notes"
)

cursor = conn.cursor(dictionary=True)
