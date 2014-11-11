"""
    app
    ~~~

    This application is used to provide a secure web
    interface to a client. Information about the
    server's system status will be provided as well
    as the client's ability to send commands to the
    server to initialize processes.
"""

# TODO Log Server start up time in database

# Flask Imports
from flask import Flask

# Import Flask Extensions
from flask_sqlalchemy import SQLAlchemy     # Used for Object Relational Database
from flask_login import LoginManager        # Used for authorizing
from flask_moment import Moment
from flask_pagedown import PageDown
from flask_triangle import Triangle         # Used for Angularjs and jinja2

# Create Flask application object
app = Flask(__name__)

# Flask Extensions
db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()
pagedown = PageDown()
triangle = Triangle()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config):

    # Configurations
    app.config.from_object(config)

    # Init flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)
    triangle.init_app(app)

    # Import Blueprints here
    from .ctr_panel import ctr_panel_bp
    from .api import rest_api_v1_bp
    from .auth import auth_bp
    from .bist import bist_bp
    from .rec_start import rec_start_bp
    from .rec_config import rec_config_bp
    from .rec_downloader import rec_downloader_bp

    # Register blue prints here
    app.register_blueprint(ctr_panel_bp, url_prefix='/ctr',
                           template_folder='templates')
    app.register_blueprint(rest_api_v1_bp, url_prefix='/api_v1')
    app.register_blueprint(auth_bp,
                           template_folder='templates')
    app.register_blueprint(bist_bp, url_prefix='/bist',
                           template_folder='templates')
    app.register_blueprint(rec_start_bp, url_prefix='/rec_start',
                           template_folder='templates')
    app.register_blueprint(rec_config_bp, url_prefix='/rec_config',
                           template_folder='templates')
    app.register_blueprint(rec_downloader_bp, url_prefix='/rec_downloader',
                           template_folder='templates')

    db.create_all(app=app)

    return app


def get_db(config):
    app.config.from_object(config)
    db.init_app(app)
    return db