from flask import Flask, render_template, request
from threading import Thread
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('main.html')

from mongodb import get_adaklar

@app.route("/adaklar")
def adaklarSite():
    AdakList = get_adaklar()
    return render_template("adaklar.html", AdakList=AdakList)

def run():
    app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
