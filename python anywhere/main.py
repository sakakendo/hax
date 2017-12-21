
# A very simple Flask Hello World app for you to get started with...

import flask,os
from flask import Flask,request,redirect,url_for,flash
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

UPLOAD_FOLDER = '/home/sakakedo/anywhere/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','c'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
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
