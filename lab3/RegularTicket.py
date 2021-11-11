from Ticket import Ticket


class RegularTicket(Ticket):
    def __init__(self, event_name, ticket_id, price, event_date):
        super().__init__(event_name, ticket_id, price, event_date)

    def print_ticket(self):
        print(str(self))

    def __str__(self):
        return f'Regular ticket [event name = {self.event_name}, id = {self.ticket_id}, price = {self.price}, event date = {self.event_date}]'