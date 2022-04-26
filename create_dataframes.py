from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from database import Database

wavesSQL = [] #set an empty list
    
rows = Database().executeSelectQuery(tableName = 'vw_report_waves_market_prices')
for row in rows:
    wavesSQL.append(list(row))
    labels = ['Datum','Wert']
    dfwaves = pd.DataFrame.from_records(wavesSQL, columns=labels)
    dfwaves['Wert'] = dfwaves['Wert'].apply(pd.to_numeric)
    dfwaves['Datum'] = dfwaves['Datum'].apply(pd.to_datetime)

dfwaves.to_pickle("./DataFrames/dfwaves")



sharpeSQL = [] #set an empty list

rows = Database().executeSelectQuery(tableName = 'vw_report_sharpe_ratio_per_week')

for row in rows:
    sharpeSQL.append(list(row))
    labels = ['Woche', 'Kalenderwoche','Sharpe-Ratio']
    dfsharpe = pd.DataFrame.from_records(sharpeSQL, columns=labels)
    dfsharpe['Sharpe-Ratio'] = dfsharpe['Sharpe-Ratio'].apply(pd.to_numeric)

dfsharpe.to_pickle("./DataFrames/dfsharpe")