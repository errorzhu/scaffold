import os
from flasgger import swag_from
from flask import Blueprint, request, current_app, g
from flask_demo import db
from flask_demo.constant import constant
from flask_demo.models.user import User
from flask_demo.utils import response
from flask_demo.utils.auth_handler import auth

current_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))
swagger_yml_dir = os.path.join(project_dir, constant.APP_NAME, constant.SWAGGER_DOC_DIR)

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/flask/demo/api/v1/user", methods=["POST"])
@swag_from(os.path.join(swagger_yml_dir, "new_user.yml"))
def new_user():
    current_app.logger.info("create a new user")
    username = request.json.get("username")
    password = request.json.get("password")
    if username is None or password is None:
        return response.fail("username or password can not be empty", code=400)

    if User.query.filter_by(username=username).first() is not None:
        return response.fail("user already exists", code=400)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return response.success({"id": user.id, "username": user.username}, code=201)


@user_blueprint.route("/flask/demo/api/v1/user/<int:user_id>", methods=["GET"])
@swag_from(os.path.join(swagger_yml_dir, "get_user_by_id.yml"))
@auth.login_required
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return response.success({"id": user.id, "username": user.username})


@user_blueprint.route("/flask/demo/api/v1/users", methods=["GET"])
@swag_from(os.path.join(swagger_yml_dir, "get_users_by_filter.yml"))
def get_users_by_filter():
    page_size = int(request.args.get("page_size", 2 ** 20))
    page_num = int(request.args.get("page_num", 1))
    name = request.args.get("name", "*")
    user_query = User.query.with_entities(User.id, User.username)
    if name != "*":
        user_query = user_query.filter(User.username.like("%" + name + "%"))
    total = user_query.count()
    page = user_query.paginate(page_num, page_size, error_out=False)
    return response.success(
        {
            "summary": {
                "total": total
            },
            "users": [
                {
                    "id": user.id,
                    "username": user.username
                }
                for user in page.items
            ],
        }
    )


@user_blueprint.route("/flask/demo/api/v1/user/token", methods=["GET"])
@swag_from(os.path.join(swagger_yml_dir, "get_user_token.yml"))
@auth.login_required
def get_token():
    token = g.user.generate_auth_token()
    return response.success({"token": token})


@user_blueprint.route("/flask/demo/api/v1/user/<int:user_id>", methods=["DELETE"])
@swag_from(os.path.join(swagger_yml_dir, "delete_user_by_id.yml"))
def delete_user_by_id(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return response.success({"id": user.id, "username": user.username})


@user_blueprint.route("/flask/demo/api/v1/user", methods=["PUT"])
@swag_from(os.path.join(swagger_yml_dir, "update_user.yml"))
def update_user():
    username = request.json.get("username")
    password = request.json.get("password")
    user_id = request.json.get("id")
    if user_id is None:
        return response.fail("id is required!", code=400)
    user = User.query.get(user_id)
    if user is None:
        return response.fail("user does not exists!", code=400)
    if password is not None:
        user.hash_password(password)
    if username is not None:
        user.username = username
    db.session.commit()
    return response.success({"id": user.id, "username": user.username})

