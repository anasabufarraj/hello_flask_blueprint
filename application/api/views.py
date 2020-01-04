from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/api')
def hello_world() -> dict:
    return {'Hello': ', API Blueprint!'}
