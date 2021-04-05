import json

import flask

app = flask.Flask(__name__)


@app.route("/hello_world", methods=["GET"])
def get_hello_world():
    return flask.Response(status=200,
                          mimetype="application/json",
                          response=json.dumps({"text": "hello world"}))


@app.route("/data", methods=["POST"])
def post_data():
    data_dict = flask.request.get_json()
    return flask.Response(status=200,
                          mimetype="application/json",
                          response=json.dumps(data_dict))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
