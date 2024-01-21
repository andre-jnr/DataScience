# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(id='text', children='Exemplo'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Dropdown([{'label': 'All', 'value': 'ALL'},
                  {'label': 'Montreal', 'value': 'MTL'},
                  {'label': 'San Francisco', 'value': 'SF'}], 'ALL', id='dropdown'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


@app.callback(
    Output('example-graph', 'figure'),
    Input('dropdown', 'value')
)
def changeFigure(value):
    if value == 'ALL':
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    elif value == 'MTL':
        return px.bar(df[df['City'] == 'Montreal'], x='Fruit', y='Amount')
    else:
        return px.bar(df[df['City'] == 'SF'], x='Fruit', y='Amount')


if __name__ == '__main__':
    app.run(debug=True)
