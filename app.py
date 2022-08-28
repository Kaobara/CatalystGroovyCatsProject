from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')

def welcome():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def base_page():
    print(request.form)
    data = request.form
    namefm = str(data['nameformat'])
    bll = str(data['blacklist'])
    casef = str(data['CaseFormat'])
    
    return render_template("index.html")