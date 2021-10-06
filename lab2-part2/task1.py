from Product import Product
from Customer import Customer
from Order import Order


def main():
    try:
        phone = Product(1000, 'Xiaomi redmi note 8 pro', '100x30x10')
        video_card = Product(500, 'AMD Radeon rx580', '300, 100, 40')
        customer = Customer('Sarakhman', 'Artur', 'Olegovych', '+380(97)-126-62-62')
        order = Order(customer, phone, video_card)
        print('Total order value for ' + str(customer.name) + ' = ' + str(order.get_total_order_value()))
    except Exception as e:
        print(e)


main()