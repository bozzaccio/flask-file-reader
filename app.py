import os

from flask import Flask, send_file
from flask import render_template, flash, request

from src.fileconverter import convert_pdf2docx
from src.fileutils import allowed_file

app = Flask(__name__)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(ROOT_DIR, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
                pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                word_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.doc')
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                convert_pdf2docx(pdf_path, word_path)
    return send_file(word_path, as_attachment=True)


if __name__ == "__main__":
    app.run()
