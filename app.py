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

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=app.get_asset_url(def_image), style={'width': '500px', 'height': '15%'}),
    dcc.Dropdown(
        id='your-input-here',
        options=[
                {'label':list_of_choices[0], 'value':list_of_images[0]},
                {'label':list_of_choices[1], 'value':list_of_images[1]},
                {'label':list_of_choices[2], 'value':list_of_images[2]},
                {'label':list_of_choices[3], 'value':list_of_images[3]},
                {'label':list_of_choices[4], 'value':list_of_images[4]}
               ],
        value=list_of_images[4],
        style={'width': '500px'}),        
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),],
    placeholder='Select a character',)


######### Interactive callbacks go here #########
@app.callback([dash.dependencies.Output('your-output-here', 'children'),
               dash.dependencies.Output('your-input-here', 'label')],
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):


    return f'The Kung Fu Hustle character that best represents you is {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
