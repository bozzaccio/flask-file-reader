import os

from flask import render_template, flash, request, redirect

from app import app
from fileutils import allowed_file


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='PDF to Word')


@app.route('/upload', methods=['POST'])
def upload_doc():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        else:
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
            if file and allowed_file(file.filename):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect('/')
