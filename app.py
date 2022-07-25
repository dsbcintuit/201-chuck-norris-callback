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
        options=[{'label': i["label"], 'value': x} for x,i in enumerate(list_of_choices)],
        placeholder=default_text,
        value=0,
        style={'width': '500px'}),        
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.Img(src='', style={'width': '300', 'height':'200'}, id='image_choice'),
    html.Br(),
    html.A('Code on Github', href=githublink),
])


######### Interactive callbacks go here #########
@app.callback([Output('your-output-here', 'children'), 
               Output('image_choice', 'src')
              ],
              [Input('your-input-here', 'value')])

def display_value(choice_x):

    image_chosen = list_of_choices[choice_x]["image_choice"]
    text = list_of_choices[choice_x]["label"]
    return f'The Kung Fu Hustle character that best represents you is {text}.', image_chosen


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
