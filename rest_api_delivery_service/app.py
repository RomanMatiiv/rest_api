from dataclasses import dataclass


@dataclass
class Courier:
    field: int
    raise NotImplemented


@dataclass
class Order:
    field: int
    raise NotImplemented


class CourierManager:
    def __init__(self):
        raise NotImplemented

    def add_one(self, courier_id: int):
        """
        Добавляет нового курьера в систему

        Args:
            courier_id: уникальный номер курьера в системе

        Returns:
        """
        raise NotImplemented

    def add_many(self):
        """
        Добавляет несколько курьеров в систему

        Returns:

        """
        raise NotImplemented

    def change(self, courier_id: int):
        """
        Изменяет информацию у сществующего курьера

        Args:
            courier_id: уникальный номер курьера в системе

        Returns:

        """
        raise NotImplemented

    def assign_orders(self, courier_id: int):
        """
        Назначает на курьера заказы

        Args:
            courier_id:

        Returns:

        """
        raise NotImplemented

    def get_info(self):
        """
        Возвращяет информацию о курьере

        Returns:

        """
        raise NotImplemented


class OrderManager:
    def __init__(self):
        raise NotImplemented

    def add_new(self, order_id: int):
        """
        Добавляет новый заказ в систему

        Args:
            order_id: уникальныйи номер заказа в системе

        Returns:

        """
        raise NotImplemented

    def mark_done(self, order_id: int):
        """
        Помечает заказ как выполненый

        Args:
            order_id: уникальный номер заказа в системе

        Returns:

        """
        raise NotImplemented