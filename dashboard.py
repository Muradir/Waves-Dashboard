#Author: Pascal Hildebrandt
#Description: This file creates the Dashboard and interacts with all the backend data

from dash import Dash, html, dcc, dash_table
from dash_table.Format import Format
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc

dfDetails = pd.read_pickle("./backend_app/data_stores/dfcrypto")

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

# Setting up the layout in HTML Code and creating the objects, that will be created in the callbacks.
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
                    columns = [{"name": i, "id": i,
                                "type": "numeric", "format": Format(group=",", precision=2, scheme="f")}for i in dfDetails.columns],
                    style_header={
                        'backgroundColor': 'rgb(90, 90, 90)',
                        'color': 'white'
                    },
                    style_data={
                        'backgroundColor': 'rgb(50, 50, 50)',
                        'color': 'white'
                    },
                )
            ],style={'margin-left': '30px', 'backgroundColor':'#323232', "width": '70%', 'display':'inline-block'})    
        ], style = {'backgroundColor':'#323232'})
    ])
])

# The callbacks create the prior defined objects, like Graphs, Tables or Buttons.
# All interactive Objects will have one or more callbacks.

@app.callback(Output('graph', 'figure'), 
            [Input('dropdownGraph', 'value')])

# The following code will draw the Graph.
def generate_graph(dropdown):

    #choosing the correct Dataframe according to Dropdown-Value
    if dropdown == 'USD':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfusd")
    elif dropdown == 'BTC':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfbitcoin")
    elif dropdown == 'ETH':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfethereum")
    elif dropdown == 'WAVES':
        CryptoData = pd.read_pickle("./backend_app/data_stores/dfwaves")

    #loading the Dataframe and inserting the data into the graph          
    values = px.line(CryptoData, x='Date', y=CryptoData.columns, template='plotly_dark')
    values.update_layout(legend_title_text='')
    
    #adding functionality and styling to the graph
    values.update_traces(mode="lines", hovertemplate=None)
    values.update_layout(hovermode="x unified", plot_bgcolor='rgba(90, 90, 90, 90)', paper_bgcolor='rgba(50, 50, 50, 50)', hoverlabel=dict(bgcolor="gray", font_size=16, font_color="white"))
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

## The following code handles the Currency Converter.
def update_output(input1, dropdownCurrency):
    UsdValue = float

    #choosing the correct USD Value according to dropdown-field
    CurrencyData = pd.read_pickle("./backend_app/data_stores/dfconverter")
    if dropdownCurrency == 'BTC':
        UsdValue = float(CurrencyData.loc[0].at['USD'])
    elif dropdownCurrency == 'ETH':
        UsdValue = float(CurrencyData.loc[1].at['USD'])
    elif dropdownCurrency == 'WAVES':
        UsdValue = float(CurrencyData.loc[2].at['USD'])

    #returnign the calculated value (value of chosen Asset * amount of chosen assets)
    return u'It will cost you {} USD.'.format(round(UsdValue*float(input1), 2))

if __name__ == "__main__":
    app.run_server(debug=True)