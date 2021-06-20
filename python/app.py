from flask import Flask
from flask import jsonify
from flask import request
import system

app = Flask(__name__)

# Dolar 
@app.route('/login/',methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return  jsonify(system.login(username,password))
@app.route('/register/',methods = ['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    return jsonify(system.register(username,password))
  
if __name__ == '__main__':
   app.run(debug = True,port ='5000')