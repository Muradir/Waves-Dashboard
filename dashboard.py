import numbers
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Output, Input, State
from numpy import number
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

dfDetails = pd.read_pickle("./backend_app/data_stores/dfcrypto")

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

        html.Div(children=[
            html.Div(children=[
                html.H1("Converter", style={'text-align': 'center'}),
                html.I("Input asset amount and choose asset:"),
                dcc.Input(id="input1", type="number", value=0, debounce=True, required=True),
                dcc.Dropdown(
                    id='dropdownCurrency',
                    options=[
                        {'label': 'BTC', 'value': 'BTC'},
                        {'label': 'ETH', 'value': 'ETH'},
                        {'label': 'WAVES', 'value': 'WAVES'},
                    ],
                    value='BTC',
                    clearable=False,
                    searchable=False,
                    style={'color':'#323232'},
                    ),
                html.Div(id="output"),
            ],style={'backgroundColor':'#323232', "width": '25%', 'display':'inline-block', 'vertical-align':'top'}), 

            html.Div([
                html.H1("Crypto-Asset-Information", style={'text-align': 'center'}),
                dash_table.DataTable(
                    dfDetails.to_dict('records'),
                    [{"name": i, "id": i} for i in dfDetails.columns],
                    style_header={
                        'backgroundColor': 'rgb(30, 30, 30)',
                        'color': 'white'
                    },
                    style_data={
                      'backgroundColor': 'rgb(50, 50, 50)',
                      'color': 'white'
                    }
                )
            ],style={'backgroundColor':'#323232', "width": '75%', 'display':'inline-block'})    
        ])
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
    Input('input1', 'value'),
    Input('dropdownCurrency', 'value'))

def update_output(input1, dropdownCurrency):
    UsdValue = float

    CurrencyData = pd.read_pickle("./backend_app/data_stores/dfconverter")
    if dropdownCurrency == 'BTC':
        UsdValue = float(CurrencyData.loc[0].at['USD'])
    elif dropdownCurrency == 'ETH':
        UsdValue = float(CurrencyData.loc[1].at['USD'])
    elif dropdownCurrency == 'WAVES':
        UsdValue = float(CurrencyData.loc[2].at['USD'])

    return u'It will cost you {} USD.'.format(round(UsdValue*float(input1), 2))



if __name__ == "__main__":
    app.run_server(debug=True)