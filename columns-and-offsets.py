import os
from random import randint

import dash
import flask

from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html

from pandas import read_csv, DataFrame

### GLOBALS, DATA & INTIALISE THE APP ###

# Set up the Dash instance. Big thanks to @jimmybow for the boilerplate code
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(__name__, server=server)
app.config.supress_callback_exceptions = True

# Don't get online css & js
# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True

css_directory = os.getcwd()
stylesheets = ['stylesheet.css']
static_css_route = '/static/'


@app.server.route('{}<stylesheet>'.format(static_css_route))
def serve_stylesheet(stylesheet):
    if stylesheet not in stylesheets:
        raise Exception(
            '"{}" is excluded from the allowed static files'.format(
                stylesheet
            )
        )
    return flask.send_from_directory(css_directory, stylesheet)


for stylesheet in stylesheets:
    app.css.append_css({"external_url": "/static/{}".format(stylesheet)})


#cssURL = "https://rawgit.com/richard-muir/uk-car-accidents/master/road-safety.css"
# cssURL = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# app.css.append_css({
#     "external_url": cssURL
# })


SPACER_DIV = html.Div(className = 'container',style={'height' : '1em'})# spacing


app.layout = html.Div([
    html.H1('Layout Test 1'),

    'Column Width 1', 
    # Row 1
    html.Div([
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one column', style={'backgroundColor' : 'grey', 'height' : '2em'}),
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 2',
    # Row 2
    html.Div([
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 3',
    # Row 3
    html.Div([
        html.Div([], className='three columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='three columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='three columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='three columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 4',
    # Row 4
    html.Div([
        html.Div([], className='four columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='four columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='four columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),   
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 5',
    # Row 5
    html.Div([
        html.Div([], className='five columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='seven columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,
    
    'Column Width 6',
    # Row 6
    html.Div([
        html.Div([], className='six columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='six columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 7',
    # Row 7
    html.Div([
        html.Div([], className='seven columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='five columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 8',
    # Row 8
    html.Div([
        html.Div([], className='eight columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='four columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 9',
    # Row 9
    html.Div([
        html.Div([], className='nine columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='three columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 10',
    # Row 10
    html.Div([
        html.Div([], className='ten columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 11',
    # Row 11
    html.Div([
        html.Div([], className='eleven columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),
        html.Div([], className='one columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),        
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Column Width 12',
    # Row 12
    html.Div([
        html.Div([], className='twelve columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),       
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,
    SPACER_DIV,

    'Offset by 1',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-one eleven columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 2',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-two ten columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

        'Offset by 3',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-three nine columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 4',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-four eight columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 5',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-five seven columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 6',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-six six columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 7',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-seven five columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 8',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-eight four columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 9',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-nine three columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 10',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-ten two columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,

    'Offset by 11',
    # Row 13
    html.Div([
        html.Div([], className='offset-by-eleven one columns', style={'backgroundColor' : 'grey', 'height' : '2em'}),            
    ],
    className = 'container',
    style={
        'border' : '1px solid black'
    }),
    SPACER_DIV,
    

])

# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
