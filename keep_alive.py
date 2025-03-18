from flask import Flask, render_template
from threading import Thread
import random
from main import application 

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('main.html')

from i import ilist 
x = ilist.keys()

@app.route("/i")
def images():
    return render_template('images.html', x=x)

from mongodb import get_adaklar
import os

@app.route("/adaklar")
def adaklarSite():
    AdakList = get_adaklar()
    return render_template("adaklar.html", AdakList=AdakList)

app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
application()
# Importing the library

def keep_alive():
    '''
	Creates and starts new thread that runs the function run.
	'''
    t = Thread(target=run)
    t.start()
    # a = Thread(target=ram)
    # a.start()
