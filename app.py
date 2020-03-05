# app.py
from flask import Flask, request, jsonify
import yahoofinanceAPI

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return 'HEJ!!!'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)