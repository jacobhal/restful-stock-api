# app.py
from flask import Flask, request, jsonify
import alphavantageAPI
import yahoofinanceAPI

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    response = jsonify({'DATA': '<h1>This is a financial stock API</h1>'})
    return response

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)