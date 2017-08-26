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

# Include the external CSS
cssURL = "https://rawgit.com/richard-muir/uk-car-accidents/master/road-safety.css"
app.css.append_css({
    "external_url": cssURL
})
