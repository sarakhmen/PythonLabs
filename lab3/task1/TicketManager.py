import os
import json

import datetime

from TicketFactory import TicketFactory
from Ticket import Ticket


class TicketManager:

    def __init__(self, tickets_filename):
        self.__ticket_factory = None
        self.__load_tickets(tickets_filename)

    @property
    def tickets(self):
        return self.__tickets

    @staticmethod
    def __validate_filename(filename):
        if not isinstance(filename, str):
            raise TypeError('filename must be of type str')
        if not filename.endswith('.json'):
            raise ValueError('invalid json file name')

    def __load_tickets(self, filename):
        if not isinstance(filename, str):
            raise TypeError('filename must be of type str')
        if not filename.endswith('.json'):
            raise ValueError('invalid json file name')
        self.__tickets_filename = filename
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                self.__tickets = json.load(f, object_hook=self.__decode_ticket)
        else:
            self.__tickets = list()

    def save_ticket(self, ticket_to_save):
        self.__tickets.append(ticket_to_save)
        with open(self.__tickets_filename, "w") as f:
            json.dump(self.__tickets, f, default=self.__encode_ticket, indent=4)

    def get_factory_instance(self):
        if self.__ticket_factory is None:
            ticket_id = max(self.__tickets, key=lambda x: x.ticket_id).ticket_id if len(self.tickets) != 0 else 0
            self.__ticket_factory = TicketFactory(ticket_id)
        return self.__ticket_factory

    @staticmethod
    def __encode_ticket(ticket):
        if isinstance(ticket, Ticket):
            ticket_dict = {"Ticket": ticket.__class__.__name__,
                           "event name": ticket.event_name,
                           "id": ticket.ticket_id,
                           "price": ticket.price,
                           "event date": ticket.event_date.isoformat()
                           }
            return ticket_dict

    @staticmethod
    def __decode_ticket(dct):
        if 'Ticket' in dct:
            return TicketFactory.load_ticket(dct)
        return dct
