######### Import your libraries #######
import dash
from dash import dcc, html, Input, Output, State
import os

###### Set up variables
list_of_choices=[
    {
        "label": 'Sing',
        "image": 'mainguy.jpeg'
    },
    {
        "label": 'Landlady',
        "image": 'landlady.jpeg'
    },
    {
        "label": 'Landlord',
        "image": 'husband.jpeg'
    },
    {
        "label": 'The Beast',
        "image": 'frog.jpeg'
    },
    {
        "label": 'The Tailor',
        "image": 'ringsguy.jpeg'
    }
]
 
githublink = 'https://github.com/dsbcintuit/201-chuck-norris-callback'
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
        options=[{'label': i["label"], 'value': j} for j,i in enumerate(list_of_choices)],
        value=0,
        style={'width': '500px'},
        placeholder=default_text,),        
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.Img(src='', style={'width': '300', 'height':'200'}, id='image-output'),
    html.Br(),
    html.A('Code on Github', href=githublink),
])


######### Interactive callbacks go here #########
@app.callback([Output('your-output-here', 'children'), 
               Output('image-output', 'src')
              ],
              [Input('your-input-here', 'value')])

def display_value(value):

    image = list_of_choices[choice_j]["image"]
    text = list_of_choices[choice_i]["label"]
    return f'The Kung Fu Hustle character that best represents you is {text}.', image


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
