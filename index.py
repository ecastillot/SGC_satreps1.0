import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import home

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    requests_pathname_prefix='/'
)
app.title= 'SATREPS'
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.A(html.Button('Go to SATREPS'),className='go_to_satreps',href='/home/'),
    html.Div(id='page-content'),
])