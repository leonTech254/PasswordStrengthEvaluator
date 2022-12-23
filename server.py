from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
from password import PasswordChecker

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resorces={r'/*': {"orgins": '*'}})



@app.route("/")
def home():
    return "password strength evaluater"


@app.route("/password-checker", methods=['GET', 'POST'])
def password_checker():
    if request.method=="POST":
        contents=request.get_json()
        user_password=contents["password"]
        data = PasswordChecker.input_passwod(user_password)
        return jsonify({"response":data})
    return "check password strength"


app.run(debug=True)
