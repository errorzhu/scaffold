import json
import pytest

header = {"Content-Type": "application/json"}


def test_new_user(client):
    data = {"username": "zhuyu", "password": "1234"}
    rv = client.post("/flask/demo/api/v1/user", data=json.dumps(data), headers=header)
    assert "success" == rv.json["status"]
    assert "zhuyu" == rv.json["data"]["username"]


def test_get_user_by_id(client, auth_tool):
    data = {"username": "zhuyu", "password": "1234"}
    rv = client.post("/flask/demo/api/v1/user", data=json.dumps(data), headers=header)
    assert "success" == rv.json["status"]
    assert "zhuyu" == rv.json["data"]["username"]
    auth_header = auth_tool.get_auth_header("zhuyu", "1234")
    auth_header = {**auth_header, **header}
    rv = client.get("/flask/demo/api/v1/user/1", headers=auth_header)
    assert "success" == rv.json["status"]
    assert "zhuyu" == rv.json["data"]["username"]


def test_get_user_by_filter(client):
    data = {"username": "zhuyu", "password": "1234"}
    rv = client.post("/flask/demo/api/v1/user", data=json.dumps(data), headers=header)
    assert "success" == rv.json["status"]
    assert "zhuyu" == rv.json["data"]["username"]
    rv = client.get("/flask/demo/api/v1/users?name=y", headers=header)
    assert "success" == rv.json["status"]
    assert "zhuyu" == rv.json["data"]["users"][0]["username"]


if __name__ == '__main__':
    pytest.main(["./test_user.py"])
