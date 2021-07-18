from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin


from marshmallow import Schema, fields


import json

import flask

app = flask.Flask(__name__)

spec = APISpec(title="Swagger hello world",
               version="1.0.0",
               openapi_version="3.0.2",
               plugins=[FlaskPlugin(), MarshmallowPlugin()],
               )


class HelloWorldSchema(Schema):
    text = fields.Str()


@app.route("/hello_world", methods=["GET"])
def get_hello_world():
    """
    Тестовая функция
    ---
    get:
      description: Get a hello world massage
      responses:
        200:
          content:
            application/json:
              schema: HelloWorldSchema
    """
    return flask.Response(status=200,
                          mimetype="application/json",
                          response=json.dumps({"text": "hello world"}))


# @app.route("/data", methods=["POST"])
# def post_data():
#     data_dict = flask.request.get_json()
#     return flask.Response(status=200,
#                           mimetype="application/json",
#                           response=json.dumps(data_dict))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
