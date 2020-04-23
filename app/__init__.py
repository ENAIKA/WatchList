from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

#application initialization
app = Flask(__name__, instance_relative_config = True)

#Configuration setting
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
from app import error
