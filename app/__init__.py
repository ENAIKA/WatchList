from flask import Flask
from .config import DevConfig

#application initialization
app = Flask(__name__, instance_relative_config = True)

#Configuration setting
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
