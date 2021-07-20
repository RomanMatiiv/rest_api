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
                description: 'OK'
                content:
                    application/json:
                        schema: HelloWorldSchema
    """

    #TODO разобраться как возвращать обект
    # HelloWorldSchema().dump(hello_world_object)

    return flask.Response(status=200,
                          mimetype="application/json",
                          response=json.dumps({"text": "hello world"}))


@app.route("/data", methods=["POST"])
def post_data():
    """
    Возвращает ровно то, что принимает
    ---
    get:
        description: Возвращает ровно то, что принимает
        responses:
            200:
                description: 'OK'
    """
    data_dict = flask.request.get_json()
    return flask.Response(status=200,
                          mimetype="application/json",
                          response=json.dumps(data_dict))


# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=get_hello_world)
    spec.path(view=post_data)


if __name__ == "__main__":
    print(spec.to_yaml())

    app.debug = True
    app.run(host="0.0.0.0", port=8080)
