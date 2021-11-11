from Ticket import Ticket


class StudentTicket(Ticket):
    def __init__(self, ticket_id, price, event_date):
        super().__init__(ticket_id, price, event_date)

    def print_ticket(self):
        print(str(self))

    def __str__(self):
        return f'Student ticket [id = {self.ticket_id}, price = {self.price}, event date = {self.event_date}]'
