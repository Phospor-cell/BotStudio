import os

from flask import Flask
app = Flask(__name__, template_folder='templates')
app.config.["SECRET_KEY"] = "Take a secret key"
from  app import routes