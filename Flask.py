from datetime import datetime
from flask import Flask, request
import json
import hashlib

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def registeruser():
    users = load_users()
    login = request.form.get('login')
    password = request.form.get('password')
    try:
        users[login]
        return {'status': 'error, this user already exists'}, 400
    except KeyError:
        users[login] = {}
        users[login]['password'] = hashlib.sha256(password.encode('utf-8')).hexdigest()
        users[login]['date'] = str(datetime.now())
        
    save_users(users)
    return {'status': 'success'}, 200

@app.route('/user', methods=['GET'])
def getusers():
    users = load_users()
    if not users:
        return {'status': 'no registered users'}
    return load_users()

def load_users():
    with open('users.json', 'r') as file:
        return json.load(file)

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)