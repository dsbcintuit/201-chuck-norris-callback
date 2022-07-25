######### Import your libraries #######
import dash
from dash import dcc, html, Input, Output, State
import os

###### Set up variables
list_of_choices=['Sing', 'Landlady', 'Landlord', 'The Beast', 'The Tailor']
githublink = 'https://github.com/dsbcintuit/201-chuck-norris-callback'
list_of_images=['mainguy.jpeg', 'landlady.jpeg', 'husband.jpeg', 'frog.jpeg', 'ringsguy.jpeg']
heading1='Which Kung Fu Hustle Character Are You?'
tabtitle='Tha Hustle'
def_image='poster.jpeg'
default_text="Select a character"

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=app.get_asset_url(def_image), style={'width': '400px', 'height': '15%'}),
    dcc.Dropdown(
        id='your-input-here',
        options=(id='your-input-here',
                options=[{'label': list_of_choices[i], 'value': i} for i in range(len(list_of_choices))],
                value=list_of_choices[0],
                style={'width': '500px'},
        placeholder=default_text,),        
    html.Br(),
    html.Div(id='your-output-here', children=''),
    # html.Div(id='your-output-here', image=''),
    html.Br(),
    html.Img(id='image-output', src=app.get_asset_url(list_of_images[0])),
    html.Br(),
    html.A('Code on Github', href=githublink),
])


######### Interactive callbacks go here #########
@app.callback([Output('your-output-here', 'children'), 
               Output('image-output', 'src')
              ],
              [Input('your-input-here', 'value')])

def display_value(whatever_you_chose):

    # return html.Img(src=app.get_asset_url(whatever_you_chose), style={'width': '400px', 'height': '15%'}),
    return f'The Kung Fu Hustle character that best represents you is {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
