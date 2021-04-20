"""
В данном модуле реализованна аналитическая часть
"""


class Analytic:
    def __init__(self):
        raise NotImplemented

    def get_rating(self, courier_id: int):
        """
        Возвращает рейтинг курьера

        TODO добавить формулу расчета

        Args:
            courier_id: уникальный номер курьера в системе

        Returns:

        """
        raise NotImplemented

    def get_salary(self, courier_id: int):
        """
        Возвращает кол-во денег, полученных курьером

        TODO добавить формулу расчета

        Args:
            courier_id: уникальный номер курьера в системе

        Returns:

        """
        raise NotImplemented
