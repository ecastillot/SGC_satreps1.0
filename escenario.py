import flask
import json

with open('config.json') as cfg:
    cfg_dict = json.load(cfg)
    static_folder = cfg_dict['static_folder']
    prehtml_file = static_folder.split('/')[-1]
    html_file = f'{prehtml_file}_mts.html'


flask_app = flask.Flask(__name__,
            static_url_path='', 
            static_folder= static_folder,
            template_folder= static_folder)
            # static_folder='/mnt/escenarios/21192022202020_3.92694_77.74589_M8.5_30km/html/21192022202020',
            # template_folder='/mnt/escenarios/21192022202020_3.92694_77.74589_M8.5_30km/html/21192022202020')

@flask_app.route('/')
def index():
    return flask.render_template(html_file)
    # return flask.render_template('21192022202020_mts.html')
    # # return 'Hello Flask app'

if __name__ == "__main__":
    print(html_file)