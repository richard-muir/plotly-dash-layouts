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

])

# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
