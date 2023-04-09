from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

root_dir = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template('index.html')