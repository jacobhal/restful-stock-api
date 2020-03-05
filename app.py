# app.py
from flask import Flask, request, jsonify
import alphavantageAPI
# import yahoofinanceAPI

app = Flask(__name__)

@app.route('/getinfo', methods=['GET'])
def info_response():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    res = {}

    if not equity:
        res["ERROR"] = "No equity specified."
    else:
        # info = yahoofinanceAPI.get_info(equity)
        res["DATA"] = 'info'

    response = jsonify(res)
    return response   

@app.route('/search', methods=['GET'])
def search_response():
    # Retrieve the equity from url parameter
    keywords = request.args.get("keywords", None)
    res = {}

    if not keywords:
        res["ERROR"] = "No search keywords specified."
    else:
        search_results = alphavantageAPI.search(keywords)
        res["DATA"] = search_results

    response = jsonify(res)
    return response 

@app.route('/gethistory', methods=['GET'])
def history_response():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    period = request.args.get("period", None)
    if period is None:
        period = "max"
    res = {}

    if not equity:
        res["ERROR"] = "No equity specified."
    else:
        # history = yahoofinanceAPI.get_history(equity, period)
        res["DATA"] = 'history'

    response = jsonify(res)
    return response  

@app.route('/gethistoryalpha', methods=['GET'])
def history_response_alpha():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    function = request.args.get("function", None)
 
    res = {}

    if not equity:
        res["ERROR"] = "No equity specified."
    elif not function:
        res["ERROR"] = "No function specified."
    else:
        history = alphavantageAPI.get_history(equity, function)
        res["DATA"] = history

    response = jsonify(res)
    return response

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