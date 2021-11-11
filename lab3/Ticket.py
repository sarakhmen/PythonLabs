from abc import ABC, abstractmethod
from datetime import date


class Ticket(ABC):
    def __init__(self, ticket_id, price, event_date):
        self.__set_id(ticket_id)
        self.__set_price(price)
        self.__set_event_date(event_date)

    def __set_id(self, ticket_id):
        if not isinstance(ticket_id, int):
            raise TypeError('ticket_id must be of type int')
        if ticket_id <= 0:
            raise ValueError('ticket_id must be greater than 0')
        self.__ticket_id = ticket_id

    def __set_price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError('price must be of type int or float')
        if price < 0:
            raise ValueError('price must be greater than or equal 0')
        self.__price = float(price)

    def __set_event_date(self, event_date):
        if not isinstance(event_date, date):
            raise TypeError('event date must be of type date')
        self.__event_date = event_date

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def price(self):
        return self.__price

    @property
    def event_date(self):
        return self.__event_date

    @abstractmethod
    def print_ticket(self):
        pass
