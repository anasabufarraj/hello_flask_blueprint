from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/auth')
def hello_world() -> str:
    return 'Hello, Auth Blueprint!'
