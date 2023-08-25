#!/usr/bin/python3

from flask import Flask 
from flask import render_template
from flask import request
from reader import readit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input_form_r.html')

@app.route('/read', methods=['POST'])
def process_c_inputs():
    source = request.form.get('source')
    destination = request.form.get('destination')
    cpassword = request.form.get('cpassword')
    # Do something with the input

    readit(source, destination, cpassword)

    return "Complete! Check your destination folder!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

