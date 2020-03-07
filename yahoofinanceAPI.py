import yfinance as yf
import pandas as pd
import sys

def get_info(equity):
    
    res = {}
    try:
        company = yf.Ticker(equity)

        # get stock info
        res["INFO"] = company.info
        # show actions (dividends, splits)
        res["ACTIONS"] = company.actions.to_json()
        res["DIVIDENDS"] = company.dividends.to_json()
        res["SPLITS"] = company.splits.to_json()
        res["FINANCIALS"] = company.financials.to_json()
        res["QUARTERLY_FINANCIALS"] = company.quarterly_financials.to_json()
        res["MAJOR_HOLDERS"] = company.major_holders.to_json()
        res["INSTITUTIONAL_HOLDERS"] = company.institutional_holders.to_json()
        res["BALANCE_SHEET"] = company.balance_sheet.to_json()
        res["QUARTERLY_BALANCE_SHEET"] = company.quarterly_balance_sheet.to_json()
        res["CASHFLOW"] = company.cashflow.to_json()
        res["QUARTERLY_CASHFLOW"] = company.quarterly_cashflow.to_json()
        res["EARNINGS"] = company.earnings.to_json()
        res["QUARTERLY_EARNINGS"] = company.quarterly_earnings.to_json()
        res["SUSTAINABILITY"] = company.sustainability.to_json()
        company.recommendations.reset_index(inplace=True)
        res["RECOMMENDATIONS"] = company.recommendations.to_json()
        res["CALENDAR"] = company.calendar.to_json()
        res["ISIN"] = company.isin
        res["OPTIONS"] = company.options
    except ValueError:
        res["ERROR"] = "Equity does not exist."
    
    return res

def get_history(equity, period):
    company = yf.Ticker(equity)
    # get historical market data
    return company.history(period=period).to_json()

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

