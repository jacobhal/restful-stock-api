import yfinance as yf
import pandas as pd
import sys
import json

def get_info(equity):
    
    res = {}
    success = False
   
    try:
        company = yf.Ticker(equity)

        # get stock info
        res["INFO"] = company.info
        # show actions (dividends, splits)
        res["ACTIONS"] = json.loads(company.actions.to_json())
        res["DIVIDENDS"] = json.loads(company.dividends.to_json())
        res["SPLITS"] = json.loads(company.splits.to_json())
        res["FINANCIALS"] = json.loads(company.financials.to_json())
        res["QUARTERLY_FINANCIALS"] = json.loads(company.quarterly_financials.to_json())
        res["MAJOR_HOLDERS"] = json.loads(company.major_holders.to_json())
        if "INSTITUTIONAL_HOLDERS" in res:
            res["INSTITUTIONAL_HOLDERS"] = json.loads(company.institutional_holders.to_json())
        res["BALANCE_SHEET"] = json.loads(company.balance_sheet.to_json())
        res["QUARTERLY_BALANCE_SHEET"] = json.loads(company.quarterly_balance_sheet.to_json())
        res["CASHFLOW"] = json.loads(company.cashflow.to_json())
        res["QUARTERLY_CASHFLOW"] = json.loads(company.quarterly_cashflow.to_json())
        res["EARNINGS"] = json.loads(company.earnings.to_json())
        res["QUARTERLY_EARNINGS"] = json.loads(company.quarterly_earnings.to_json())
        res["SUSTAINABILITY"] = json.loads(company.sustainability.to_json())
        company.recommendations.reset_index(inplace=True)
        res["RECOMMENDATIONS"] = json.loads(company.recommendations.to_json())
        res["CALENDAR"] = json.loads(company.calendar.to_json())
        res["HISTORY"] = json.loads(company.history(period='max').to_json())
        res["ISIN"] = company.isin
        res["OPTIONS"] = company.options
        success = True
    except:
        res["ERROR"] = "Something went wrong... (the requested equity might not exist)."
    
    return res, success

def get_history(equity, period):
    res = {}
    try:
        company = yf.Ticker(equity)
         # get historical market data
        return json.loads(company.history(period=period).to_json()), True
    except:
        res["ERROR"] = "Something went wrong... (the requested equity might not exist)."
        return res, False


def get_actions(equity):
    company = yf.Ticker(equity)
    return company.actions

def get_dividends(equity):
    company = yf.Ticker(equity)
    return company.dividends

def get_splits(equity):
    company = yf.Ticker(equity)
    return company.splits

def get_financials(equity):
    company = yf.Ticker(equity)
    return company.financials

def get_quarterly_financials(equity):
    company = yf.Ticker(equity)
    return company.quarterly_financials

def get_major_holders(equity):
    company = yf.Ticker(equity)
    return company.major_holders

def get_institutional_holders(equity):
    company = yf.Ticker(equity)
    return company.institutional_holders

def get_balance_sheet(equity):
    company = yf.Ticker(equity)
    return company.balance_sheet

def get_quarterly_balance_sheet(equity):
    company = yf.Ticker(equity)
    return company.quarterly_balance_sheet

def get_cashflow(equity):
    company = yf.Ticker(equity)
    return company.cashflow

def get_quarterly_cashflow(equity):
    company = yf.Ticker(equity)
    return company.quarterly_cashflow

def get_earnings(equity):
    company = yf.Ticker(equity)
    return company.earnings

def get_quarterly_earnings(equity):
    company = yf.Ticker(equity)
    return company.financials

def get_sustainability(equity):
    company = yf.Ticker(equity)
    return company.sustainability

def get_recommendations(equity):
    company = yf.Ticker(equity)
    return company.recommendations

def get_calendar(equity):
    company = yf.Ticker(equity)
    return company.calendar

def get_isin(equity):
    company = yf.Ticker(equity)
    return company.isin

def get_options(equity):
    company = yf.Ticker(equity)
    return company.options

def option_chain(equity, expiration):
    company = yf.Ticker(equity)
    # # get option chain for specific expiration
    opt = company.option_chain(expiration)
    # # data available via: opt.calls, opt.puts

