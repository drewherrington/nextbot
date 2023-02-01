#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from main import predict_class, get_response

intents = json.load(open('intents.json'))

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({'health': 'ok'})


@app.route('/', methods=['POST', 'OPTIONS'])
def chat():
    if (request.data):
        content = request.get_json(silent=True)
        message = content['body']
    else:
        message = request.form['body']
    ints = predict_class(message)
    response = app.response_class(
        response=json.dumps(get_response(ints, intents)),
        status=200,
        mimetype='application/json'
    )
    return response
