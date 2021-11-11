from datetime import date


class Event:
    def __init__(self, event_name, event_id, standard_price, event_date):
        self.__set_event_name(event_name)
        self.__set_event_id(event_id)
        self.__set_standard_price(standard_price)
        self.__set_date(event_date)

    @property
    def event_name(self):
        return self.__event_name

    @property
    def event_id(self):
        return self.__event_id

    @property
    def standard_price(self):
        return self.__standard_price

    @property
    def date(self):
        return self.__date

    def __set_event_name(self, name):
        if not isinstance(name, str):
            raise TypeError('event name must be of type str')
        self.__event_name = name

    def __set_event_id(self, event_id):
        if not isinstance(event_id, int):
            raise TypeError('event_id must be of type int')
        if event_id <= 0:
            raise ValueError('ticket_id must be greater than 0')
        self.__event_id = event_id

    def __set_standard_price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError('price must be of type int or float')
        if price < 0:
            raise ValueError('price must be greater than or equal 0')
        self.__standard_price = float(price)

    def __set_date(self, event_date):
        if not isinstance(event_date, date):
            raise TypeError('event date must be of type date')
        self.__date = event_date

    def __str__(self):
        return f'{self.event_id} event: name = {self.event_name}, standard price = {self.standard_price}, date = {self.__date}'
