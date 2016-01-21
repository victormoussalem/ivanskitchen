from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('indexNOM.html')

@app.route('/test')
def indexNOM():
    return render_template('index.html')

@app.route('/test-1')
def imageslides():
    return render_template('image-slides.html')
