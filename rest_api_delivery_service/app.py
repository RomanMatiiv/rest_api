import json

import flask
import logging
from peewee import CharField
from peewee import FloatField
from peewee import IntegerField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import SqliteDatabase

import peewee_validates as PV

from math import inf


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = flask.Flask(__name__)


DATABASE = "delivery.db"
db = SqliteDatabase(DATABASE)


class Courier(Model):
    courier_id = PrimaryKeyField()
    courier_type = CharField()
    regions = CharField()
    working_hours = CharField()

    class Meta:
        database = db
        table_name = 'courier'


class CourierValidator(PV.ModelValidator):
    courier_id = PV.IntegerField(required=True, validators=[PV.validate_range(0, +inf)])
    courier_type = PV.StringField(required=True, validators=[PV.validate_one_of(["foot","bike","car"])])
    regions = PV.StringField(required=True)
    working_hours = PV.StringField(required=True)


class Order(Model):
    order_id = PrimaryKeyField()
    weight = FloatField()
    region = IntegerField()
    delivery_hours = CharField()

    class Meta:
        database = db
        table_name = 'order'


class OrderValidator(PV.ModelValidator):
    order_id = PV.IntegerField(required=True, validators=[PV.validate_range(0, +inf)])
    weight = PV.FloatField(required=True, validators=[PV.validate_range(0, +inf)])
    region = PV.IntegerField(required=True, validators=[PV.validate_range(0, +inf)])
    delivery_hours = PV.StringField(required=True)


class CourierManager:
    def __init__(self):
        raise NotImplemented

    def add_one(self, courier_data: dict) -> Courier:
        """
        Добавляет нового курьера в систему

        Args:
            courier_data:

        Returns:
        """
        # TODO добавить проверки
        courier_id = int(courier_data["courier_id"])
        courier_type = courier_data["courier_type"]
        regions = str(courier_data["regions"])
        working_hours = str(courier_data["working_hours"])

        logger.info(f"saving courier with id={courier_id}")
        courier = Courier(courier_id=courier_id,
                          courier_type=courier_type,
                          regions=regions,
                          working_hours=working_hours)

        return courier

    def extract_id(self, failed_couriers) -> list:
        """
          [{"id": 1}, {"id": 2}, {"id": 3}]

        Args:
            failed_couriers:

        Returns:

        """
        pass

    @app.route("/couriers", methods=["POST"])
    def add_many(self):
        """
        Добавляет несколько курьеров в систему

        Returns:

        """
        fail = False

        raw_data = flask.request.get_json()
        data = json.loads(raw_data)
        all_courier = data["data"]

        success_couriers = []
        failed_couriers = []

        logger.info("start saving couriers")
        for raw_courier in all_courier:
            raw_courier = json.loads(raw_courier)

            courier = self.add_one(raw_courier)

            validator = CourierValidator(courier)
            if validator.validate():
                success_couriers.append(courier)
            else:
                fail = True
                failed_couriers.append(courier)

        if fail:
            couriers_id = self.extract_id(failed_couriers)
            couriers_id = {"couriers": couriers_id}
        else:
            couriers_id = self.extract_id(success_couriers)
            couriers_id = {"couriers": couriers_id}

        if fail:
            status = 400
            response = {"validation_error": couriers_id}
        else:
            status = 201
            response = couriers_id

        return flask.Response(status=status,
                              mimetype="application/json",
                              response=json.dumps(response))

    @app.route("/couriers/<int:courier_id>", methods=["PATCH"])
    def change(self, courier_id: int):
        """
        Изменяет информацию у сществующего курьера

        Args:
            courier_id: уникальный номер курьера в системе

        Returns:

        """
        raise NotImplemented

    @app.route("/orders/assign", methods=["POST"])
    def assign_orders(self, courier_id: int):
        """
        Назначает на курьера заказы

        Args:
            courier_id:

        Returns:

        """
        raise NotImplemented

    @app.route("/couriers/<int:courier_id>", methods=["GET"])
    def get_info(self, courier_id: int):
        """
        Возвращяет информацию о курьере

        Returns:

        """
        raise NotImplemented


class OrderManager:
    def __init__(self):
        raise NotImplemented

    def add_one(self, order_id: int):
        """
        Добавляет новый заказ в систему

        Args:
            order_id: уникальныйи номер заказа в системе

        Returns:

        """
        raise NotImplemented

    @app.route("/orders", methods=["POST"])
    def add_many(self):
        """
        """
        raise NotImplemented

    @app.route("/orders/complete", methods=["POST"])
    def mark_done(self, order_id: int):
        """
        Помечает заказ как выполненый

        Args:
            order_id: уникальный номер заказа в системе

        Returns:

        """
        raise NotImplemented


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
