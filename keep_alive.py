from flask import Flask, render_template
from threading import Thread
import random


app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <style>* {
        background: #333;
        color: white;
        text-align: center;
        font-family: sans-serif;
        font-size: 90px;
    }
    body {
        height: 100vh;
    	display: flex;
    	justify-content: center;
    	align-items: center;
    }
    h1 {
        position: relative;
    }
    </style>
    <body>
    <h1>Yakında</h1>
    </body>
    """

from i import ilist 
x = ilist.keys()
len = len(x)

@app.route("/i")
def images():
    return render_template('images.html', x=x, len=len)


def run():
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def keep_alive():
    '''
	Creates and starts new thread that runs the function run.
	'''
    t = Thread(target=run)
    t.start()
