from datetime import date, datetime
from StudentTicket import StudentTicket
from RegularTicket import RegularTicket
from LateTicket import LateTicket
from AdvanceTicket import AdvanceTicket


class TicketFactory:
    def __init__(self, last_id):
        self.__set_last_id(last_id)

    def __set_last_id(self, last_id):
        if not isinstance(last_id, int):
            raise TypeError('last id must be of type int')
        if last_id < 0:
            raise ValueError('last id must be greater than or equal 0')
        self.__last_id = last_id

    def create_ticket(self, price, event_date, is_student=False):
        self.__validate_is_student(is_student)
        self.__validate_price(price)
        today = date.today()
        self.__validate_date(today, event_date)

        day_difference = (event_date - today).days
        self.__last_id += 1

        if is_student:
            return StudentTicket(self.__last_id, price * 0.5, event_date)
        elif day_difference >= 60:
            return AdvanceTicket(self.__last_id, price * 0.6, event_date)
        elif day_difference < 10:
            return LateTicket(self.__last_id, price * 1.1, event_date)
        else:
            return RegularTicket(self.__last_id, price, event_date)

    @staticmethod
    def load_ticket(ticket_dict):
        ticket_id = ticket_dict['id']
        price = ticket_dict['price']
        event_date = datetime.strptime(ticket_dict['event date'], '%Y-%m-%d').date()

        ticket_name = ticket_dict['Ticket']
        if ticket_name == 'StudentTicket':
            return StudentTicket(ticket_id, price, event_date)
        elif ticket_name == 'AdvanceTicket':
            return AdvanceTicket(ticket_id, price, event_date)
        elif ticket_name == 'LateTicket':
            return LateTicket(ticket_id, price, event_date)
        elif ticket_name == 'RegularTicket':
            return RegularTicket(ticket_id, price, event_date)
        else:
            raise ValueError('unknown ticket')

    @staticmethod
    def __validate_is_student(is_student):
        if not isinstance(is_student, bool):
            raise TypeError('is_student must be of type bool')

    @staticmethod
    def __validate_price(price):
        if not isinstance(price, (float, int)):
            raise TypeError('price must be of type int or float')
        if price < 0:
            raise ValueError('price must be greater than or equal 0')

    @staticmethod
    def __validate_date(today, event_date):
        if not isinstance(event_date, date):
            raise TypeError('event date must be of type date')
        if today > event_date:
            raise TypeError('event is over')

