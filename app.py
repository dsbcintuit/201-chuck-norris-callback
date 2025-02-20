######### Import your libraries #######
import dash
from dash import dcc, html, Input, Output, State
import os

###### Set up variables
list_of_choices=['Sing', 'Landlady', 'Landlord', 'The Beast', 'The Tailor']
list_of_images=['mainguy.jpeg', 'landlady.jpeg', 'husband.jpeg', 'frog.jpeg', 'ringsguy.jpeg']
githublink = 'https://github.com/dsbcintuit/201-chuck-norris-callback'
image1='poster.jpeg'
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
    html.Img(id='image-output', src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
	    dcc.Dropdown(id='your-input-here',	
                options=[{'label': list_of_choices[i], 'value': i} for i in range(len(list_of_choices))],	
                value=list_of_choices[0],	
                style={'width': '500px'},
                placeholder='Select an option'),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):
    return f'The Kung Fu Hustle character that best represents you is {list_of_choices[whatever_you_chose]}.'


@app.callback(dash.dependencies.Output('image-output', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])

def display_value(whatever_you_chose):
    return app.get_asset_url(list_of_images[whatever_you_chose])

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)