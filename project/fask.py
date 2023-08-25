#!/usr/bin/python3

from flask import render_template
from flask import request
from flask import Flask
from create_config import create_c
from reader import readit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read', methods=['POST'])
def dis():
    return render_template('input_request_r.html')

@app.route('/process_r_inputs', methods=['POST'])
def process_r_inputs():
    source = request.form.get('source')
    destination = request.form.get('destination')  # Make sure you use the correct variable name

    readit(source, destination)

    return "Complete! Check your destination folder!"

@app.route('/process_inputs', methods=['POST'])
def disp():
    return render_template('input_request_c.html')

@app.route('/process_c_inputs', methods=['POST'])
def process_c_inputs():
    source = request.form.get('source')
    destination = request.form.get('destination')

    # Do something with the input

    create_c(source, destination)

    return "Complete! Check your destination folder!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

