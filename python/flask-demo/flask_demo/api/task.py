import os
from flasgger import swag_from
from flask import Blueprint, request, current_app, g
from flask_socketio import emit

from flask_demo import db, socketio
from flask_demo.constant import constant
from flask_demo.models.task import Task
from flask_demo.models.user import User
from flask_demo.utils import response

current_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))
swagger_yml_dir = os.path.join(project_dir, constant.APP_NAME, constant.SWAGGER_DOC_DIR)

task_blueprint = Blueprint("task", __name__)


@task_blueprint.route("/flask/demo/api/v1/tasks", methods=["GET"])
@swag_from(os.path.join(swagger_yml_dir, "get_tasks_by_filter.yml"))
def get_tasks_by_filter():
    page_size = int(request.args.get("page_size", 2 ** 20))
    page_num = int(request.args.get("page_num", 1))
    task_query = Task.query.with_entities(
        Task.id, Task.name, Task.user_id, User.username
    ).join(User, Task.user_id == User.id)

    total = task_query.count()
    page = task_query.paginate(page_num, page_size, error_out=False)
    return response.success(
        {
            "summary": {"total": total},
            "tasks": [
                {
                    "id": task.id,
                    "taskname": task.username,
                    "user_id": task.user_id,
                    "username": task.username,
                }
                for task in page.items
            ],
        }
    )


@socketio.on("task")
def get_socket_data(message):
    id = message["id"]
    emit("task", {"data": id})
