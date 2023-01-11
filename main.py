from flask import Flask
from flask import request
import os
app = Flask(__name__)
ctf_flag = os.environ.get('admin_flag')
@app.route('/v1/user/info')
def get_flag():
    print(request.headers)
    API_KEY = request.headers['x-api-key']
    if API_KEY == '$API_KEY' :
        return ctf_flag


@app.route('/verify/user/<userId>', methods=['POST'])
def verify_password():
    data = request.form
    user = data['user']
    password = data['password']

    if user == '$user' & password == '$password' :
        return "Login seccessful"
    return "invalid crendential"

if __name__ == '__main__':
	app.run()
