import mysql.connector

print("input mysql host: (default = 'localhost')")
input_host = str(input())
if (input_host == ''): input_host = 'localhost'
print("input mysql user: (default = 'username')")
input_user = str(input())
if (input_user == ''): input_user = 'root'
print("input mysql input_password: (default = 'password')")
input_password = str(input())
if (input_password == ''): input_password = 'password'
print("input mysql database for flashcards: (default = 'db')")
input_database = str(input())
if (input_database == ''): input_database = 'db'

db = mysql.connector.connect(
	host=input_host,
	user=input_user,
	password=input_password,
	database=input_database)

cursor = db.cursor()

query = "CREATE TABLE users (UUID VARCHAR(36) PRIMARY KEY, name VARCHAR(100), password VARCHAR(50), profile_pic_path VARCHAR(256),CONSTRAINT unique_name UNIQUE (name));"

cursor.execute(query)
db.commit()

query = "CREATE TABLE decks (UUID VARCHAR(36) PRIMARY KEY,name VARCHAR(100),user VARCHAR(100),custom_cover BOOL,last_activity VARCHAR(100));"

cursor.execute(query)
db.commit()

query = "CREATE TABLE cards (UUID VARCHAR(36) PRIMARY KEY,deck VARCHAR(100),user VARCHAR(100),queue INTEGER,f_pic1_path VARCHAR(50),f_pic2_path VARCHAR(50),f_text TEXT,b_pic1_path VARCHAR(50),b_pic2_path VARCHAR(50),b_text TEXT);"

cursor.execute(query)
db.commit()

print('success')