import requests
import os

api_key = os.environ.get('API_KEY', None)

base_url = 'https://www.alphavantage.co/query'

def get_history(equity, function, csv = False):
    payload = {'function' : function, 'symbol' : equity, 'apikey' : api_key}
    if csv:
        payload['datatype'] = 'csv'
    response = {}
    success = False
    try:
        response = requests.get(base_url, params=payload)
        success = True
    except:
        response["ERROR"] = "Something went wrong..."
    if "Error Message" in response:
        success = False
    return response.json(), success

def search(keywords, csv = False):
    payload = {'function' : "SYMBOL_SEARCH", 'keywords' : keywords, 'apikey' : api_key}
    if csv:
        payload['datatype'] = 'csv'
    response = {}
    success = False
    try:
        response = requests.get(base_url, params=payload)
        success = True
    except:
        response["ERROR"] = "Something went wrong..."
    if "Error Message" in response:
        success = False
    return response.json(), success


# urls = {
#     fetchUrl: '',
#     apikey: '2IZ7T22DCQJIF88Y',


#     // This API returns intraday time series (timestamp, open, high, low, close, volume) of the equity specified.
#     intradayData: 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo',

#     /*
#     This API returns daily time series (date, daily open, daily high, 
#     daily low, daily close, daily volume, daily adjusted close, and split/dividend events) of the global equity specified
#     */
#     historicalDataDaily: 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey=demo&datatype=csv',


#     /*
#     This API returns weekly adjusted time series (last trading day of each week, weekly open, weekly high, 
#     weekly low, weekly close, weekly adjusted close, weekly volume, weekly dividend) of the global equity specified
#     */
#     historicalDataWeekly: 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=MSFT&apikey=demo&datatype=csv',

#     /*
#     This API returns monthly adjusted time series (last trading day of each month, monthly open, monthly high, 
#     monthly low, monthly close, monthly adjusted close, monthly volume, monthly dividend) of the equity specified
#     */
#     historicalDataMonthly: 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=MSFT&apikey=demo&datatype=csv',

#     /*
#     A lightweight alternative to the time series APIs, 
#     this service returns the latest price and volume information for a security of your choice.
#     */
#     lightWeightLatest: 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=demo',

#     /*
#     We've got you covered! The Search Endpoint returns the best-matching symbols and market information based on keywords of your choice. 
#     The search results also contain match scores that provide you with the full flexibility to develop your own search and filtering logic.
#     */
#     searchEndpoint: 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BA&apikey=demo&datatype=csv',


#     testUrl: 'https://restful-stock-api.herokuapp.com/getmsg/?name=Jacob'
# }