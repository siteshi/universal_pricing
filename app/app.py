from flask import Flask, render_template, jsonify, request
import os
import pandas as pd
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def calculate():
    #file = request.files['image']
    return

if __name__ == "__main__":
    app.run(debug=True,port=5002)