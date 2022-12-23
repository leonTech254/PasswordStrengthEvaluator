from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from password import PasswordChecker

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resorces={r'/*': {"orgins": '*'}})

app = Flask(__name__)


@app.route("/")
def home():
    return "password strength evaluater"


@app.route("/password-checker", methods=['GET', 'POST'])
def password_checker():
    data = PasswordChecker.input_passwod("martin")
    return data


app.run(debug=True)
