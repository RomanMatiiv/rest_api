"""
В данном модуле реализованна логика работы с курьерами
"""


class CourierManage:
    def __init__(self):
        raise NotImplemented

    def add_new_courier(self, courier_id: int):
        """
        Добавляет нового курьера в систему

        Args:
            courier_id: уникальный номер курьера в системе

        Returns:
        """
        raise NotImplemented

    def change_courier(self, courier_id: int):
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
