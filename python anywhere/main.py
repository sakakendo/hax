
# A very simple Flask Hello World app for you to get started with...

import flask,os,io
from flask import Flask,request,redirect,url_for,flash,jsonify
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPDigestAuth
from werkzeug.utils import secure_filename

app = Flask(__name__)
bauth = HTTPBasicAuth()
#app.config['XXXXX'] = 'XXXXX'
app.config['SECRET_KEY'] = 'XXXXX'
dauth = HTTPDigestAuth()
users = {
    "XXX": "xxx",
    "YYY": "yyy"
}

@bauth.get_password
def bget_pw(username):
    if username in users:
        return users.get(username)
    return None
@dauth.get_password
def dget_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/basic')
@bauth.login_required
def basic():
    return 'hello basic<p><input type="button" value="push me" onclick="alert();"></p>'

@app.route('/digest')
@dauth.login_required
def digest():
    return 'hello digest<p><input type="button" value="push me" onclick="alert();"></p>'
@app.route('/digest/coockie')
@dauth.login_required
def dsession():
    return '<p>cookie </p><script src="javascript">console.log(document.coockie);</script><br><p>end of cookie</p>'

@app.route('/upload/', methods=['POST','GET'])
def upload():
    if request.method == 'GET':
        return 'post me'
    if request.files is not None :
        return 'input is'+request.files
#        for file in request.files:
#            return_value.join(file)
#        return 'input_value is'+return_value
    else:
        return "no input file"
@app.route('/uploaded')
def uploaded():
    files = os.listdir('/home/sakakendo/anywhere/files')
    return ''.join(files)

@app.route('/')
def index():
    return '''
        Hello from Flask!<br><a href=/>index.html</a><br><a href=/basic>/basic</a><br>
        <a href=/digest>/digest</a><br><a href=/uploads>uploads</a>
        <p><input type="button" value="push me" onclick="alert();"></p>
        <input type="file" name="file" id="file" value="file""></p>
        '''

@app.route('/home')
def home():
    return flask.render_template('index.html')



















