######### Import your libraries #######
import dash
from dash import dcc, html, Input, Output, State
import os

###### Set up variables
list_of_options=['Sing', 'Landlady', 'Landlord', 'The Beast', 'The Tailor']
list_of_images=['mainguy.jpeg', 'landlady.jpeg', 'husband.jpeg', 'frog.jpeg', 'ringsguy.jpeg']
githublink = 'https://github.com/dsbcintuit/201-chuck-norris-callback'
# image1='poster.jpeg'
heading1='Which Kung Fu Hustle Character Are You?'
tabtitle='Tha Hustle'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(id='image', src=app.get_asset_url(list_of_images[0]), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
        options=[
                {'label':list_of_options[0], 'value':list_of_images[0]},
                {'label':list_of_options[1], 'value':list_of_images[1]},
                {'label':list_of_options[2], 'value':list_of_images[2]},
                {'label':list_of_options[3], 'value':list_of_images[3]},
                {'label':list_of_options[4], 'value':list_of_images[4]}
                ],
        value=list_of_options[0],
        placeholder='Select option...',
        style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback([dash.dependencies.Output('your-output-here', 'children')],
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):
    return f'Chuck Norris will now execute you with a {whatever_you_chose}.'


@app.callback(dash.dependencies.Output('image', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):
    return app.get_asset_url(list_of_images[whatever_you_chose])

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)