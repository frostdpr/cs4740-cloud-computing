#!/usr/bin/env python
import os, subprocess
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      if f.filename != 'add.go':
         return 'Your file must be named add.go'
      f.save(secure_filename(f.filename))
      orig_sub = ''
      with open('add.go','r') as fs:
         for line in fs:
            orig_sub += line + '<br/>'

      subprocess.call("rm -f ./a.out", shell=True)
      retcode = subprocess.call("./test.sh", shell=True)
      output = "Score: " + str(retcode) + " out of 2 correct.<br/>" + "*************Original submission*************<br/>" + orig_sub

     
      return output
		
if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')

