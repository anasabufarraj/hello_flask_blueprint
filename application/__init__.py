from flask import Flask
from application.api import api, views
from application.auth import auth, views

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(auth, url_prefix='/auth')
