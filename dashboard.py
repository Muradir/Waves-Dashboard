from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from database_depr import Database

app = Dash(__name__)
server = app.server

## Im folgenden Abschnitt wird das Layout des Dashboards festegelegt und mit HTML-Code definiert.
app.layout = dbc.Container([
    html.Div([
        html.H1("Cryptodashboard", style={'text-align': 'center'}),
        html.Div([
            html.H1("Market prices", style={'text-align': 'center'}),
            dcc.Interval(id='update_interval', interval=1*30000),
            html.Div(style={"width": '20%'}, children=[
                dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'USD', 'value': 'USD'},
                    {'label': 'BTC', 'value': 'BTC'},
                    {'label': 'ETH', 'value': 'ETH'},
                    {'label': 'WAVES', 'value': 'WAVES'},
                ],
                value='USD',
                clearable=False,
                searchable=False,
                style={'color':'#323232'},
               )               
            ]),
            dcc.Graph(id='graph', figure=go.Figure(layout=dict(plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)'))),
            
            ],style={'backgroundColor':'#323232'}),
        html.Div([
            dcc.Graph(id='apy', figure=go.Figure(layout=dict(plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)'))),
        ]),   
    ])    
])

##Durch die Callbacks werden die Graphen mit Hilfe des Plotly Dash Frameworks erzeugt. Im App Layout werden dann nach dem Aufrufen der Callbacks die Graphen aktualisiert und angezeigt.

@app.callback(Output('graph', 'figure'), 
            [Input('dropdown', 'value')])

##Der folgende Code wird innerhalb des Callbacks ausgeführt und "zeichnet" den Graphen.

def generate_graph_waves(dropdown):

    if dropdown == 'USD':
        CryptoData = pd.read_pickle("./DataFrames/dfusd")
    elif dropdown == 'BTC':
        CryptoData = pd.read_pickle("./DataFrames/dfbitcoin")
    elif dropdown == 'ETH':
        CryptoData = pd.read_pickle("./DataFrames/dfethereum")
    elif dropdown == 'WAVES':
        CryptoData = pd.read_pickle("./DataFrames/dfwaves")
        
    values = px.scatter(CryptoData, x='Datum', y='Wert', trendline='rolling', trendline_options=dict(window=7), trendline_color_override="crimson", template='plotly_dark') 

    values['data'][0]['showlegend']=True
    values['data'][1]['showlegend']=True
    values['data'][0]['name']='Waves'
    values['data'][1]['name']='MA 7'

    values.update_traces(mode="lines", hovertemplate=None)
    values.update_layout(hovermode="x unified", plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)', hoverlabel=dict(bgcolor="gray", font_size=16, font_color="white"))
    #waves.update_yaxes(title_text="Wert in USD")
    values.update_xaxes(
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
    return values

@app.callback(Output('apy', 'figure'), 
    [Input('update_interval', 'interval')])

def generate_graph_apy(self):
    apySQL = []
    rows = Database().executeSelectQuery(tableName = 'vw_report_waves_apy')
    records = []
    timeframes = [1, 3, 7, 30, 60]
    for i in range(0, len(timeframes)):
        records.append((timeframes[i], rows[0][i]))

    for row in records:
        apySQL.append(list(row))
        labels = ['Zeitraum in Tagen', 'APY']
        dfapy = pd.DataFrame.from_records(apySQL, columns=labels)
        dfapy['APY'] = dfapy['APY'].apply(pd.to_numeric)
       
    apy = px.bar(dfapy, x='Zeitraum in Tagen', y='APY', template='plotly_dark')
    apy.update_layout(plot_bgcolor='rgba(90, 90, 90, 90)',paper_bgcolor='rgba(50, 50, 50, 50)')
    apy.update_traces(marker_color='crimson')
    apy.update_xaxes(type='category')

    return apy

if __name__ == "__main__":
    app.run_server(debug=True)