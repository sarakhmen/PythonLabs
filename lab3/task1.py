from datetime import date

from RegularTicket import RegularTicket
from TicketFactory import TicketFactory
from TicketManager import TicketManager
from EventProvider import EventProvider


def main():
    events = EventProvider.load_events('events.json')
    print(*events, sep='\n')
    manager = TicketManager('tickets.json')
    factory = manager.get_factory_instance()
    ticket1 = factory.create_ticket(1000, date(2022, 2, 10), True)
    manager.save_ticket(ticket1)
    for t in manager.tickets:
        t.print_ticket()


main()
