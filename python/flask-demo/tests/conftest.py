import os
import tempfile
import pytest
from flask_demo import create_app, db
import base64


class AuthTool:

    def get_auth_header(self, user, password):
        raw = user + ":" + password
        encode = base64.b64encode(raw.encode())
        return {"Authorization": "Basic " + encode.decode("utf8")}


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app("testing")
    yield app
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app("testing")

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def auth_tool():
    return AuthTool()
