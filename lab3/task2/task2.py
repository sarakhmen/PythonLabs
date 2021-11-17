from OrderManager import OrderManager
from PizzaManager import PizzaManager

customer = 'Artur Sarakhman'


def input_option():
    return int(input('Please enter an option:\n'
                     '1 - order pizza-of-the-day\n'
                     '2 - get all orders\n'
                     '3 - exit\n'))


def main():
    order_manager = OrderManager()
    while True:
        try:
            option = input_option()
            if option == 1:
                addons = []
                addons_price = 0
                if input('Would you like something to add Y/N ?').lower() == 'y':
                    for k, v in PizzaManager.addons.items():
                        if input(f'Would you like to add {k}({v}₴) Y/N ?').lower() == 'y':
                            addons.append(k)
                            addons_price += v
                order_manager.order_pizza(customer, addons_price, addons)

            elif option == 2:
                print('Your orders:')
                print(*order_manager.orders, sep='\n\n')
            elif option == 3:
                print('Ok, goodbye!')
                break
            else:
                raise ValueError('Unknown option')

        except Exception as e:
            print('Sorry, I didn\'t understand that. Error message: ' + str(e))

        input('\nEnter something to continue...\n')


main()
