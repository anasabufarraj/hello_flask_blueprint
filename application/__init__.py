from flask import Flask
from application.api.views import api
from application.auth.views import auth

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(auth, url_prefix='/auth')
