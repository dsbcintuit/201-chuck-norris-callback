######### Import your libraries #######
import dash
from dash import dcc
from dash import html
import os

###### Set up variables
list_of_choices=['Sing', 'Landlady', 'Landlord', 'The Beast', 'The Tailor']
githublink = 'https://github.com/dsbcintuit/201-chuck-norris-callback'
image1='poster.jpg'
list_of_images=['mainguy.jpg', 'landlady.jpg', 'husband.jpg', 'frog.jpg', 'ringsguy.jpg']
heading1='Which Kung Fu Hustle Character Are You?'
tabtitle='Tha Hustle'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div(children=[
    html.H2(heading1),
    html.Img(src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
                options=[
                {'label':list_of_choices[0], 'value':list_of_choices[0]},
                {'label':list_of_choices[1], 'value':list_of_choices[1]},
                {'label':list_of_choices[2], 'value':list_of_choices[2]},
                {'label':list_of_choices[3], 'value':list_of_choices[3]},
                {'label':list_of_choices[4], 'value':list_of_choices[4]},
                ],
                value=list_of_images[4],
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'The Kung Fu Hustle character that best represents you is {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
