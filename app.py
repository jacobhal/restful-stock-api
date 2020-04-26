# app.py
from flask import Flask, request, jsonify
import alphavantageAPI
import yahoofinanceAPI
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING', None)
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import (Stock, StockSchema)

def update_or_add_stock(equity, field, data):
    equity = equity.upper()
    existing_stock = db.session.query(Stock).filter(Stock.equity == equity).one()
    if existing_stock is None:
        if field == 'info':
            stock = Stock(equity=equity, info=data)
        elif field == 'history':
            stock = Stock(equity=equity, history=data)
        elif field == 'history_alpha':
            stock = Stock(equity=equity, history_alpha=data)
        db.session.add(stock)
    else:
        if field == 'info':
            existing_stock.info = data
        elif field == 'history':
            existing_stock.history = data
        elif field == 'history_alpha':
            existing_stock.history_alpha = data
    db.session.commit()


@app.route('/getinfo', methods=['GET'])
def info_response():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    res = {}
    success = False

    if not equity:
        res["ERROR"] = "No equity specified."
    else:
        info, success = yahoofinanceAPI.get_info(equity)
        res["DATA"] = info
    response = jsonify(res)

    if success: 
        update_or_add_stock(equity, 'info', info)

    return response   

@app.route('/search', methods=['GET'])
def search_response():
    # Retrieve the equity from url parameter
    keywords = request.args.get("keywords", None)
    res = {}

    if not keywords:
        res["ERROR"] = "No search keywords specified."
    else:
        search_results, success = alphavantageAPI.search(keywords)
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
    success = False

    if not equity:
        res["ERROR"] = "No equity specified."
    else:
        history, success = yahoofinanceAPI.get_history(equity, period)
        res["DATA"] = history
    response = jsonify(res)

    if success: 
        update_or_add_stock(equity, 'history', history)

    return response  

@app.route('/gethistoryalpha', methods=['GET'])
def history_response_alpha():
    # Retrieve the equity from url parameter
    equity = request.args.get("equity", None)
    function = request.args.get("function", None)
 
    res = {}
    success = False

    if not equity:
        res["ERROR"] = "No equity specified."
    elif not function:
        res["ERROR"] = "No function specified."
    else:
        history, success = alphavantageAPI.get_history(equity, function)
        res["DATA"] = history
    response = jsonify(res)

    if success: 
        update_or_add_stock(equity, 'history_alpha', history)

    return response

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