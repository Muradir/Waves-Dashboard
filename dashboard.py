import numbers
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from numpy import number
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
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
                id='dropdownGraph',
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

        html.Div(style={"width": '20%'}, children=[
            html.I("Input Dollar Value:"),
            html.Br(),
            dcc.Input(id="input1", type="number", placeholder="", debounce=True),
            dcc.Dropdown(
                id='dropdownCurrency',
                options=[
                    {'label': 'BTC', 'value': 'BTC'},
                    {'label': 'ETH', 'value': 'ETH'},
                    {'label': 'WAVES', 'value': 'WAVES'},
                ]),
            html.Div(id="output")
        ]),   
    ])    
])

##Durch die Callbacks werden die Graphen mit Hilfe des Plotly Dash Frameworks erzeugt. Im App Layout werden dann nach dem Aufrufen der Callbacks die Graphen aktualisiert und angezeigt.

@app.callback(Output('graph', 'figure'), 
            [Input('dropdownGraph', 'value')])

##Der folgende Code wird innerhalb des Callbacks ausgeführt und "zeichnet" den Graphen.

def generate_graph(dropdown):

    if dropdown == 'USD':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfusd")
    elif dropdown == 'BTC':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfbitcoin")
    elif dropdown == 'ETH':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfethereum")
    elif dropdown == 'WAVES':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfwaves")
        
    #values = px.line(CryptoData, x='Date', y=['BTC', 'ETH', 'WAVES', 'SP500'], template='plotly_dark')  
    values = px.line(CryptoData, x='Date', y=CryptoData.columns, template='plotly_dark')
    values.update_layout(legend_title_text='')

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

@app.callback(
    Output('output', 'children'),
    Input('dropdownCurrency', 'value'),
    Input('input1', 'value')
)

def update_output(input1):
    return u'Input 1 {}'.format(input1)

if __name__ == "__main__":
    app.run_server(debug=True)