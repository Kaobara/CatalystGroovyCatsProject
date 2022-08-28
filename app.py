from unicodedata import name
from flask import Flask, render_template, request
from main import backend

app = Flask(__name__)

@app.route('/')

def welcome():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def base_page():
    print(request.form)
    data = request.form
    namefm = data['nameformat']
    bll = data['blacklist']
    casef = str(data['CaseFormat'])
    addnum = data['AddNumbers']
    symbol = str(data['Symbol'])
        
    print(type(namefm))
    print(namefm)
    result = backend(namefm, bll, casef, addnum, symbol)
    print(result)
    return render_template("index.html")