import importlib
import os
import sys
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, Response
from flasgger import Swagger
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from flask_demo.utils import response


current_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(os.path.join(project_dir, "etc"))
config_module = importlib.import_module("config")
config = config_module.config


# auth for flasgger
def requires_basic_auth(f):
    def check_auth(username, password):
        return username == "admin" and password == "admin"

    def authenticate():
        return Response(
            "Authentication required.",
            401,
            {"WWW-Authenticate": "Basic realm='Login Required'"},
        )

    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


swagger = Swagger(decorators=[requires_basic_auth])
db = SQLAlchemy()
socketio = SocketIO()


def create_app(config_name="development"):
    app = Flask(__name__)
    swagger.init_app(app)
    CORS(app, supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # be careful to use "'"
    socketio.init_app(app, cors_allowed_origins='*')

    @app.errorhandler(404)
    def not_found(e):
        return response.fail("url not found", code=404)

    @app.errorhandler(Exception)
    def global_exception(e):
        return response.fail(repr(e), code=500)

    from flask_demo.api.user import user_blueprint
    from flask_demo.api.task import task_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)
    return app
