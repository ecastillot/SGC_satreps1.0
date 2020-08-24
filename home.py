import pandas as pd
import os
import numpy as np
import dash                     #(version 1.0.0)
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as py     #(version 4.4.1)
import plotly.graph_objs as go
import json

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    requests_pathname_prefix='/home/'
)

mapbox_access_token = 'pk.eyJ1IjoiZWNhc3RpbGxvdCIsImEiOiJjazk1cWtienowcDIxM2VwdXlnNW9yeXluIn0.mDKOxssrWB_OJeCICgi3yg'
df = pd.read_csv("/home/ecastillo/git/SGC/SGC_satreps/code/csv/datos-satreps.csv")

app.title= 'SATREPS'

blackbold={'color':'black', 'font-weight': 'bold'}

app.layout = html.Div([
    html.Div([ 
        html.H1('SATREPS',className='title'),
        

    ], className='twelve columns'
    ),
#---------------------------------------------------------------
# Map_legen + Profundidad_checklsist + Magnitud_checklist + Web_link + Map
    html.Div([
        html.Div([
            
            # Magnitud_checklist
            html.Label(children=['Magnitud: '], style=blackbold),
            dcc.Checklist(id='mag',
                options=[{'label':str(b),'value':b} for b in sorted(df['magnitud'].unique())],
                #value=[b for b in sorted(df['magnitud'].unique())],
                value=[],
            ),

            # Profundidad_type_checklist
            html.Label(children=['Profundidad: '], style=blackbold),
            dcc.Checklist(id='prof',
                options=[{'label':str(b),'value':b} for b in sorted(df['profundidad'].unique())],
                #value=[b for b in sorted(df['profundidad'].unique())]
                value=[],
            className='three columns'),
            
            # Map-legend
            html.Ul([
                html.Li("", className='circle', style={'background': '#D10000','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("", className='circle', style={'background': '#E25D00','color':'black',
                    'list-style':'none','text-indent': '17px','white-space':'nowrap'}),
                html.Li("", className='circle', style={'background': '#E6B900','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("", className='circle', style={'background': '#08C900','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("", className='circle',  style={'background': '#00C9B8','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("", className='circle',  style={'background': '#0087C9','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("", className='circle',  style={'background': '#3C00C9','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("", className='circle',  style={'background': '#C800C9','color':'black',
                    'list-style':'none','text-indent': '17px'})
            ], style={'border-bottom': 'solid 3px', 'border-color':'#00FC87','padding-top': '6px'}
            ),

            html.Br(), #Espacio vertical
            
            # Web_link
            html.Label(['Website:'],style=blackbold),
            html.Pre(id='web_link', children=[],
                style={'white-space': 'pre-wrap','word-break': 'break-all',
                    'border': '1px solid black','text-align': 'center',
                    'padding': '12px 12px 12px 12px', 'color':'blue',
                    'margin-top': '3px'}
            ),

        ], className='two columns'
        ),
        
        # Map
    
        html.Div([
            dcc.Graph(id='graph', config={'displayModeBar': False, 'scrollZoom': True},
                style={'background':'#00FC87','padding-bottom':'2px','padding-left':'2px','height':'80vh'}
            )
        ], className='nine columns'
        ),
    
    ], className='row'
    ),

], className='ten columns offset-by-one'
)

#---------------------------------------------------------------
# Output of Graph
@app.callback(Output('graph', 'figure'), #component_ id= graph, component_property= figure
              [Input('mag', 'value'),
               Input('prof', 'value')])

def update_figure(chosen_boro,chosen_recycling):
    df_sub = df[(df['magnitud'].isin(chosen_boro)) &
                (df['profundidad'].isin(chosen_recycling))]

    # Create figure
    locations=[go.Scattermapbox(
                    lon = df_sub['longitud'],
                    lat = df_sub['latitud'],
                    mode='markers',
                    #marker={'color' : df_sub["colorp"]},
                    #marker=go.scattermapbox.Marker(size= 20, color= df_sub["colorp"]),
                    marker = dict(symbol="circle",size=20,opacity=0.8,color=df_sub["colorp"]),
                    unselected={'marker' : {'opacity':0.9}},
                    selected={'marker' : {'opacity':0.5, 'size':35}},
                    hoverinfo='text',
                    hovertext=df_sub["zfolder"],
                    customdata=df_sub['zfolder']
    )]

    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision= 'foo', #preserves state of figure/map after callback activated
            clickmode= 'event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Escenarios",font=dict(size=30, color='#006479')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                style='light',
                center=dict(
                    lat=3.75294,
                    lon=-78.54337
                ),
                pitch=0,
                zoom=5
            ),
        )
    }



#---------------------------------------------------------------
# callback for Web_link
@app.callback(
    Output('web_link', 'children'),
    [Input('graph', 'clickData')])
def display_click_data(clickData):
    if clickData is None:
        return 'Select an event'
    else:
        
        the_link = clickData['points'][0]['customdata'].strip()
        html_folder = the_link.split('_')[0]
        static_folder = os.path.join('/mnt','escenarios',
                                    the_link,
                                    'html',
                                    html_folder)
        if the_link is None:
            return 'No Website Available'
        else:
            # return html.A(the_link, href=the_link, target="_blank")
            cfg_dict = {'static_folder': str(static_folder)}
            with open("config.json", "w") as cfg:  
                json.dump(cfg_dict, cfg) 
            return html.A(static_folder, href='escenario', target="_blank")
# #--------------------------------------------------------------




if __name__ == '__main__':
    app.run_server(debug=True, host='10.100.100.11', port = 8050)



