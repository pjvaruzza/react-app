import os
from flask import Flask
from flask_cors import CORS

from .utils import Config

# application factory for flask app
def create_app():
    config_object = Config()
    app = Flask(__name__)

    # Cross-Origin Config
    CORS(app,
        origins=[config_object.CORS_ALLOW_ORIGIN], # the domains allowed to access the server
        supports_credentials=config_object.CORS_SUPPORTS_CREDENTIALS) # True

    # Set the configurations
    app.config.from_object(config_object)

    # load the routes we defined in 'routes/main.py' into the app
    from .routes import main
    app.register_blueprint(main)
    return app
