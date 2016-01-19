from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/NOM')
def indexNOM():
    return render_template('indexNOM.html')
