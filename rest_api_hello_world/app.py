import json
import logging

import flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

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
        description: возвращяет hello_world
        responses:
            200:
                description: 'OK'
                content:
                    application/json:
                        schema: HelloWorldSchema
    """

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


def setup_logger() -> None:
    logging.basicConfig(level=logging.DEBUG)


# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=get_hello_world)
    spec.path(view=post_data)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    setup_logger()

    logger.info("start")

    _kwargs = {'allow_unicode': True}
    yaml_spec = spec.to_yaml(yaml_dump_kwargs=_kwargs)
    logger.debug(f"yaml openapi scpec:\n{yaml_spec}")
    logger.debug(f"type yaml spec: {type(yaml_spec)}")

    openapi_file_name = "openapi.yaml"
    logger.info(f"saving openapi spec to file: {openapi_file_name}")
    with open(openapi_file_name, "w", encoding="UTF8") as f:
        f.write(yaml_spec)

    app.debug = True
    app.run(host="0.0.0.0", port=8080)
    logger.info("end")
