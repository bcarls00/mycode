#!/usr/bin/python3

from flask import Flask 
from flask import render_template
from flask import request
from create_config import create_c

app = Flask(__name__)

@app.route('/create')
def index():
    return render_template('input_form.html')

@app.route('/read')
def process_r_inputs():
    source = request.form.get('source')
    destination = request.form.get('source')

    read(source, destination)

    return "Complete! Check your destination folder!"

@app.route('/process_inputs', methods=['POST'])
def process_c_inputs():
    source = request.form.get('source')
    destination = request.form.get('destination')

    # Do something with the input

    create_c(source, destination)

    return "Complete! Check your destination folder!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

