# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request

# import Dropzone
from flask_dropzone import Dropzone

app = Flask(__name__)
# initialize dropzone
dropzone = Dropzone(app)

app.config.update(
    UPLOADED_PATH=os.getcwd() + '/uploads',
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_INPUT_NAME='photo',
    DROPZONE_MAX_FILES=30,
    DROPZONE_CLICKABLE='false'
)

# set the route
@app.route('/', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('photo')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='localhost', port=9393)
