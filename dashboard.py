from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import pyodbc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import mysql.connector
import threading, time



def connectSQLServer(driver, server, db, user, pw):
    connSQLServer = pyodbc.connect(
        r'DRIVER={' + driver + '};'
        r'SERVER=' + server + ';'
        r'DATABASE=' + db + ';'
        r'UID=' + user + ';'
        r'PWD=' + pw + ';'
        r'Trusted_Connection=yes;',
        autocommit=True
    )
    return connSQLServer 

load_figure_template(["darkly"])

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    html.Div(children=[
        html.H1("Finanzdashboard", style={'text-align': 'center'}),
        dcc.Interval(id='update_interval', interval=1*30000),
        html.Div([
            html.H1("Waves - Dollar", style={'text-align': 'center'}),
            dcc.Graph(id='waves-graph', figure=go.Figure(layout=dict(plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)'))),
            dcc.Graph(id='sharpe-graph', figure=go.Figure(layout=dict(plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)')))
                ]),
        html.Div([
            dcc.Graph(id='sentiment-graph', figure=go.Figure(layout=dict(plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)'))),   
        ]),
        html.Div([

        ])    
    ])    
])

@app.callback(Output('waves-graph', 'figure'), 
            [Input('update_interval', 'interval')])

def generate_graph_waves(self):
      
    wavesSQL = [] #set an empty list

    sql_conn = connectSQLServer('MySQL ODBC 8.0 ANSI Driver', 'bp1o15l1iwoajeyerhf6-mysql.services.clever-cloud.com:3306', 'bp1o15l1iwoajeyerhf6', 'u122k7mhfbxvt0rp', 'sYLq0OQvnWYw8Lv56bB6') 
    cursor = sql_conn.cursor()
    cursor.execute("SELECT weightedAveragePrice, date FROM vw_report_waves_market_prices")
    rows = cursor.fetchall()
    for row in rows:
        wavesSQL.append(list(row))
        labels = ['Wert','Datum']
        dfwaves = pd.DataFrame.from_records(wavesSQL, columns=labels)
        dfwaves['Wert'] = dfwaves['Wert'].apply(pd.to_numeric)
        dfwaves['Datum'] = dfwaves['Datum'].apply(pd.to_datetime)
    cursor.close
    sql_conn.close

    waves = px.scatter(dfwaves, x='Datum', y='Wert', trendline='rolling', trendline_options=dict(window=10), trendline_color_override="crimson", template='plotly_dark') 
    waves_ma20 = px.scatter(dfwaves, x='Datum', y='Wert', trendline='rolling', trendline_options=dict(window=20),  template='plotly_dark')
    x_ma20 = waves_ma20["data"][1]['x']
    y_ma20 = waves_ma20["data"][1]['y']
    waves.add_trace(go.Line(x=x_ma20, y=y_ma20))
    waves_ma50 = px.scatter(dfwaves, x='Datum', y='Wert', trendline='rolling', trendline_options=dict(window=50), template='plotly_dark')
    x_ma50 = waves_ma50["data"][1]['x']
    y_ma50 = waves_ma50["data"][1]['y']
    waves.add_trace(go.Line(x=x_ma50, y=y_ma50))
    waves_ma100 = px.scatter(dfwaves, x='Datum', y='Wert', trendline='rolling', trendline_options=dict(window=100), template='plotly_dark')
    x_ma100 = waves_ma100["data"][1]['x']
    y_ma100 = waves_ma100["data"][1]['y']
    waves.add_trace(go.Line(x=x_ma100, y=y_ma100))

    waves['data'][0]['showlegend']=True
    waves['data'][1]['showlegend']=True
    waves['data'][0]['name']='Waves'
    waves['data'][1]['name']='MA 10'
    waves['data'][2]['name']='MA 20'
    waves['data'][3]['name']='MA 50'
    waves['data'][4]['name']='MA 100'

    waves.update_traces(mode="lines", hovertemplate=None)
    waves.update_layout(hovermode="x unified", plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)', hoverlabel=dict(bgcolor="gray", font_size=16, font_color="white"))
    waves.update_yaxes(title_text="Wert in USD")
    waves.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ]),
            bgcolor="dimgray"
        )
    )
    print("Aktuelle Daten in die Datenbank gespeichert!") 
    return waves

@app.callback(Output('sharpe-graph', 'figure'), 
        [Input('update_interval', 'interval')])

def generate_graph_sharpe(self):
    sharpeSQL = [] #set an empty list

    sql_conn = connectSQLServer('MySQL ODBC 8.0 ANSI Driver', 'bp1o15l1iwoajeyerhf6-mysql.services.clever-cloud.com:3306', 'bp1o15l1iwoajeyerhf6', 'u122k7mhfbxvt0rp', 'sYLq0OQvnWYw8Lv56bB6') 
    cursor = sql_conn.cursor()
    cursor.execute("SELECT value, date FROM vw_core_market_treasury_yield")
    rows = cursor.fetchall()
    for row in rows:
        sharpeSQL.append(list(row))
        labels = ['Wert','Datum']
        dfsharpe = pd.DataFrame.from_records(sharpeSQL, columns=labels)
        dfsharpe['Wert'] = dfsharpe['Wert'].apply(pd.to_numeric)
        dfsharpe['Datum'] = dfsharpe['Datum'].apply(pd.to_datetime)
    cursor.close
    sql_conn.close

    sharpe = make_subplots(specs=[[{"secondary_y": True}]])
    sharpe.add_trace(go.Scatter(dfsharpe, x='Datum', y='Wert'),
                    secondary_y=False,
                    )
    
    sharpe['data'][0]['showlegend']=True
    sharpe['data'][0]['name']='APY'
    sharpe['data'][0]['line']['color']="crimson"
    sharpe.update_traces(mode="lines", hovertemplate=None)
    sharpe.update_layout(hovermode="x unified", plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)', hoverlabel=dict(bgcolor="gray", font_size=16, font_color="white"))
    sharpe.update_yaxes(title_text="Wert in USD",)
    sharpe.update_yaxes
    sharpe.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ]),
            bgcolor="dimgray"
        )   
    )
    return sharpe

@app.callback(Output('sentiment-graph', 'figure'), 
        [Input('update_interval', 'interval')])

def update_graph_sentiment(self):
    sentimentSQL = []

    sql_conn = connectSQLServer('MySQL ODBC 8.0 ANSI Driver', 'bp1o15l1iwoajeyerhf6-mysql.services.clever-cloud.com:3306', 'bp1o15l1iwoajeyerhf6', 'u122k7mhfbxvt0rp', 'sYLq0OQvnWYw8Lv56bB6') 
    cursor = sql_conn.cursor()
    cursor.execute("SELECT sentimentAnalysisScore FROM vw_report_twitter_sentiment_analysis")
    rows = cursor.fetchval()
    cursor.close
    sql_conn.close

    sentiment = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0.2, 1]},
    value = rows,
    mode = "gauge+number",
    title = {'text': "Stimmung"},
    gauge = {'axis': {'range': [None, 10]},
             'bar': {'color': "gainsboro"},
             'steps' : [
                {'range': [0, 3], 'color': "crimson"},
                {'range': [3, 7], 'color': "#ffb650"},
                {'range': [7, 10], 'color': "seagreen"}],
             }))
    sentiment.update_layout(plot_bgcolor='rgba(90, 90, 90, 90)',paper_bgcolor='rgba(50, 50, 50, 50)')

    return sentiment

if __name__ == "__main__":
    app.run_server(debug=True)