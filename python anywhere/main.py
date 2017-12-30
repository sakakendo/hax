
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

@app.route('/uploads/', methods=['POST','GET'])
def upload():
    if request.method == 'GET':
        return """
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
            <form method="post">
                <div class="form-group pull-left">
                    <input type="file" id="upload_files" name="upload_files" multiple="multiple" class="form-control >
                    <p class="help-block">you can upload some files</p>
                </div>
                <div class="form-group">
                    <input type="submit" value="送信" class="form-control btn btn-primary";>
                </div>
                <div>
                    <p id="file_status">no file</p>
                    <script>
                        p=document.getElementById("file_status");
                        console.log(p.innerHTML);
                        p.innerHTML ='no file is selected';
                        console.log(p.innerHTML);

                    	$("#upload_files").bind("change", function () {
                			if (files.length==0) return false;
                    		var filelist = "";
                    		for(var i=0; i<$("#upload_files").files.length; i++){
			                    filelist += "&nbsp;&nbsp;"+$("#upload_files").files[i].name + "<br>";
		                    }
		                    p.innerHTML = filelist;
		                    console.log(fileslist);
                    		//G_files = this.files;
                    		//ファイル表示
                    		//showFiles(G_files);
                    	});
                    </script>
                </div>
            </from>
            """
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
