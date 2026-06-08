from flask import Blueprint, request, jsonify


routes = Blueprint("routes", __name__)


@routes.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "world")

    return jsonify({"message": f"Hello {name}"})


@routes.route("/exec", methods=["POST"])
def exec_cmd():

    data = request.get_json()

    cmd = data.get("cmd", "")

    return jsonify({"status": "received", "command": cmd})
