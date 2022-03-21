# Run this app with `python viz.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

sites = ['134a3fa6', '8d9fed87', '5688ed10', '2b33a48d', '07333ad0', '38c8ae33',
         'adc42b19', 'e9ba8cec', 'e12c2148', '4b78aae6', 'e724ca65', '135433c1',
         '90606897', '02ebf5c7', 'c8eb2d3d', '2b98cbdd', '39146e59', '55af2f9b',
         '28731623', '3193e230', 'e6bcf7cf', '7da0acb7', 'c18b6195', '20abb173',
         'f34b386a', 'f7f9ac09', '5fc96249', '82c74b9e', 'b255f7ad', '61bff705',
         '619fd2b9', '260f359a', '4faff963', '499a251d', 'dfc6fdf5', '64e1616f',
         '93c8a2c1', 'eec02ec5', '90791ae9', '49b6c0dd', 'd0926969', '7435e9d3']

app.layout = dash.html.Div([
    dash.html.H4('Tesla Energy - Solar Power Production Daily Monitor'),
    dash.dcc.Graph(id="time-series-chart"),
    dash.html.P("Select Site Code: "),
    dash.dcc.Dropdown(
        id="ticker",
        options=sites,
        value="134a3fa6",
        clearable=False,
    ),
])


@app.callback(
    dash.Output("time-series-chart", "figure"),
    dash.Input("ticker", "value"))
def display_time_series(ticker):
    df1 = pd.read_csv('timestamp.csv')
    fig = px.bar(df1, x='timestamp', y=ticker)
    return fig


app.run_server(debug=True, use_reloader=False)
