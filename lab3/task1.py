import os

from datetime import date

from RegularTicket import RegularTicket
from TicketFactory import TicketFactory
from TicketManager import TicketManager
from EventProvider import EventProvider


def main():
    events = EventProvider.load_events('events.json')
    manager = TicketManager('tickets.json')
    factory = manager.get_factory_instance()
    # ticket1 = factory.create_ticket(1000, date(2022, 2, 10), True)
    # manager.save_ticket(ticket1)
    # for t in manager.tickets:
    #     t.print_ticket()

    while True:
        try:
            print(*events, sep='\n')
            option = int(input('Please enter an option:\n'
                               '1 - get ticket by id\n'
                               '2 - get all tickets\n'
                               '3 - buy ticket\n'
                               '4 - exit\n'))
            if option == 1:
                ticket_id = int(input('Please enter the ticket id: '))
                print(next((x for x in manager.tickets if x.ticket_id == ticket_id),
                           f'There is no ticket with id = {ticket_id}'))
            elif option == 2:
                print('Your tickets:')
                print(*manager.tickets, sep='\n')
            elif option == 3:
                event_id = int(input('Please enter the event id the ticket you want to buy: '))
                if event_id < 1 or event_id > len(events):
                    raise ValueError('Unknown event id')
                event = events[event_id-1]
                is_student = str(input('Please enter \'+\' if you are a student: ')) == '+'
                ticket = factory.create_ticket(event.standard_price, event.date, is_student)
                manager.save_ticket(ticket)
                print(f'You have successfully bought the ticket with id = {ticket.ticket_id}')
            elif option == 4:
                print('Ok, goodbye!')
                break
            else:
                raise ValueError('Unknown option')

        except Exception as e:
            print('Sorry, I didn\'t understand that. Error message: ' + str(e))

        input('Enter something to continue...')


main()
