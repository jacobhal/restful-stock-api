# app.py
from flask import Flask, request, jsonify
import alphavantageAPI
import yahoofinanceAPI

app = Flask(__name__)

@app.route('/getinfo', methods=['GET'])
def info_response():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    response = {}

    if not equity:
        response["ERROR"] = "No equity specified."
    else:
        info = yahoofinanceAPI.get_info(equity)
        response["DATA"] = info

    return jsonify(response)    

@app.route('/gethistory', methods=['GET'])
def history_response():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    period = request.args.get("period", None)
    if period is None:
        period = "max"
    response = {}

    if not equity:
        response["ERROR"] = "No equity specified."
    else:
        history = yahoofinanceAPI.get_history(equity, period)
        response["DATA"] = history

    return jsonify(response)   

@app.route('/gethistoryalpha', methods=['GET'])
def history_response_alpha():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    function = request.args.get("function", None)
 
    response = {}

    if not equity:
        response["ERROR"] = "No equity specified."
    elif not function:
        response["ERROR"] = "No function specified."
    else:
        history = alphavantageAPI.get_history(equity, function)
        response["DATA"] = history

    return jsonify(response)   

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>This is a financial stock API</h1>"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)