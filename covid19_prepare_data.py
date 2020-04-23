import requests
from datetime import datetime
import pandas as pd

def build_covid19_data():

    dfi = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
    dfi = dfi.fillna(0)

    #states_to_skip = ['JH']
    #dfi = dfi.drop(states_to_skip, axis=1)

    dfa = dfi[dfi.Status == "Confirmed"]
    cols = dfa.columns[2:]
    for c in cols:
        dfa = dfa.rename({c: c + '_cases'}, axis=1)
    dfa = dfa.drop(['Status'], axis=1)

    dfb = dfi[dfi.Status == "Recovered"]
    cols = dfb.columns[2:]
    for c in cols:
        dfb = dfb.rename({c: c + '_recovered'}, axis=1)
    dfb = dfb.drop(['Status'], axis=1)

    dfc = dfi[dfi.Status == "Deceased"]
    cols = dfc.columns[2:]
    for c in cols:
        dfc = dfc.rename({c: c + '_deaths'}, axis=1)
    dfc = dfc.drop(['Status'], axis=1)

    dfd = pd.merge(dfa, dfb, on='Date')
    dfe = pd.merge(dfd, dfc, on='Date')

    dfe = dfe.rename({'Date': 'Report_Date'}, axis=1)
    dfe.index = pd.DatetimeIndex(dfe['Report_Date'])
    dfe = dfe.drop('Report_Date', 1)
    dfe = dfe.sort_values(by=['Report_Date'])

    dfe.to_csv('data/covid19_data.csv')
    dfe_backtesting = dfe.iloc[:-5]
    dfe_backtesting.to_csv('data/covid19_data_backtesting.csv')
    
    return dfe


