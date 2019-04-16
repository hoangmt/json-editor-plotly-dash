import json_dash
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State
import dash_html_components as html

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
#Todo: modify css to change the view of the editor the menu and searchbox
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

state = {
    'json': {
        'data':{
      'x': [1, 2, 3, 4, 5, 6],
      'y': [2, 2, 2, 4, 5,6]},
      'number': 123,
      'objects': {'a': 'a', 'b': 'b'},
      'string': 'Hello World'
    }
  }

#refer to App.js in the other project to find out the layout, not use html.Div
app.layout = html.Div(className="div",
                      children =[
html.Button('Submit', id='button'),
html.Div(dcc.Input(id='input-box', type='text')),
    json_dash.jsondash(
        id = 'json',
        json = state['json'],
        height = 400,
        width = 300,
        selected_node = ''
    ),
    html.Div('',id='node_selected')
])

@app.callback(Output('node_selected', 'children'), [Input('json', 'selected_node')])
def display_output(value):
    return 'Node selected: {}'.format(value)

@app.callback(Output('json','json'),[Input('button','n_clicks')],[State('input-box', 'value')])
def update_output(n_clicks, value):
    json = {'testing':value,'nclicks':n_clicks}
    print('finished loading data')
    return json
if __name__ == '__main__':
    app.run_server(debug=True)
