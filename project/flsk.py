#!/usr/bin/python3
from flask import Flask 
from flask import render_template
from flask import request
from create_config import create_c

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input_form.html')

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    source = request.form.get('input1')
    dest = request.form.get('input2')

    # Do something with the inputs, like processing or returning a result

    create_c(source, dest)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)

