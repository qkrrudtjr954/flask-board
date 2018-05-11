import os

from flask import Flask

# it is application factory function
def create_app(test_config=None) :
    # create and configure the app ( Flask instance )
    app = Flask(__name__, instance_relative_config=True) # tells to app that configuration files are relative to the instance folder
    app.config.from_mapping(
        SECRET_KEY='dev', # it will be override when deploying
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None :
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else :
        # load the test config if passed in
        app.config.from_mapping(test_config)
    try :
        os.makedirs(app.instance_path)
    except OSError :
        pass

    @app.route('/hello')
    def hello() :
        return 'hello world'

    # init app 
    from . import db
    db.init_app(app)

    return app
