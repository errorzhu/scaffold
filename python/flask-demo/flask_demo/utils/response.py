from flask import jsonify


def success(data, code=200):
    return jsonify({"status": "success", "data": data}), code


def fail(data, code=500):
    return jsonify({"status": "failure", "data": data}), code
