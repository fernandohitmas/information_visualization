# import packages
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Input, Output# to make tables
import plotly.express as px


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My first app with DATA and a Graph and Controls'),
    html.Hr(),
    html.Div(children)
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')    
]

# Add Controls to build interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run App
if __name__=='__main__':
    app.run(debug=True)