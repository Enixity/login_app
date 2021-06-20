import mysql.connector
import hashlib
import random
# Connection
mydb = mysql.connector.connect(
    
  host="localhost",
  
  user="root",
  
  password="",
  
  database="login_system"

)

mycursor = mydb.cursor()
    
def register(username,password):
    
    mycursor.execute("SELECT * FROM `users` WHERE `username` = '%s' " % username)


    usernameFetch = mycursor.fetchall()

    if len(usernameFetch) > 0:

        return {"error":"1","message":"username taken"}

    userID = ''.join(random.choice('0123456789ABCDEFGKLMNOP$*#!abcdefghijklmnop') for i in range(44))

    hashedPassword = hashlib.sha256(password.encode('utf8')).hexdigest()

    statment = "INSERT INTO users (username, password, userID) VALUES (%s, %s, %s)"

    values = (username, hashedPassword, userID)

    mycursor.execute(statment, values)

    mydb.commit()
    
    return {"error":"0","message":"Registered Successfully"}
    
def login(username,password):
    
    hashedPassword = hashlib.sha256(password.encode('utf8')).hexdigest()
    
    statement = ("SELECT * FROM users WHERE username = %s AND password = %s")
    
    values = (username, hashedPassword)
    
    mycursor.execute(statement,values)
    
    usernameFetch = mycursor.fetchall()
    
    if len(usernameFetch) == 0:
        
        return {"error":1,"message":"Either the username or password you entered are incorrect",}
    for row in usernameFetch:
        return {"error":0,"message":"Logged in Successfully","userID":row[1]}
