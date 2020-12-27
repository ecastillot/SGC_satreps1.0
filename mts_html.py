import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Output, Input

external_stylesheets = ['/home/ecastillo/git/SGC/SGC_satreps1.0/assets/venues_styling.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Tsunami simulation"

app.layout = html.Div([ 
    html.Div([
        dcc.Location(id='url_src1', refresh=False),
        html.A(html.H1('Tsunami simulation (source model SWIFT1)'),className='title',href='/home/mts/src1'),
        html.Table([
                html.Tr([
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                            html.Img(src="/assets/src02.jpg")
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             )
                    ]),
                html.Tr([
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             )
                    ]),
                html.Tr([
                    html.Td(),
                    html.Td(),
                    html.Td()
                    ])
            ]),
        
    ]),
    html.Div([
        dcc.Location(id='url_src2', refresh=False),
        html.A(html.H1('Tsunami simulation (source model SWIFT1)'),className='title',href='/home/mts/src1'),
        html.Table([
                html.Tr([
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             )
                    ]),
                html.Tr([
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             ),
                    html.Td("Map view of maximum tsunami heights<br>and their projections along EW and NS",
                             )
                    ]),
                html.Tr([
                    html.Td(),
                    html.Td(),
                    html.Td()
                    ])
            ]),
        
    ])

])



# app.layout = html.Div([
#     html.Div([
#         dcc.Location(id='url_src1', refresh=False),
#         html.A(html.H1('Tsunami simulation (source model SWIFT1)'),className='title',href='/home/mts/src1'),
#         html.Img(src="/assets/src02.jpg",id='src1_image')
#     ], className="image_src01")

# ], className="four.columns")

if __name__ == '__main__':
    app.run_server('10.100.100.11', 8050)