"""
SGC_satreps1.0
Es una página web creadad para visualizar los eventos del proyecto SATREPS

autores: - Emmanuel Castillo ecastillo@sgc.gov.co
         - Angel agudelo adagudelo@sgc.gov.co
04-2020
"""

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from escenario import flask_app as flask_app_scene
from home import app as dash_app_home
from index import app as dash_app_index

application = DispatcherMiddleware(dash_app_index.server, {
    '/home': dash_app_home.server,
    '/home/escenario': flask_app_scene,
})

if __name__ == '__main__':
    run_simple('10.100.100.11', 8050, application)



#REFERENCES
## https://dash.plotly.com/integrating-dash correr flask y dash simultaneamente
## http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/ crear multiples rutas en flask
## https://dash.plotly.com/sharing-data-between-callbacks compartir datos entre callbacks