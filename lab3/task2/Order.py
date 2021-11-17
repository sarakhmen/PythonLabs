from Pizza import Pizza


class Order:
    def __init__(self, order_id, customer, pizza, price, addons):
        self.order_id = order_id
        self.customer = customer
        self.pizza = pizza
        self.addons = addons
        self.price = price

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        if not isinstance(value, int):
            raise TypeError('id must be of type int')
        self.__order_id = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, str):
            raise TypeError('customer name must be of type str')
        self.__customer = customer

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError('isn`t Pizza type')
        self.__pizza = pizza

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('price must be of type int or float')
        if price < 0:
            raise ValueError('price must be greater or equal 0')
        self.__price = price

    @property
    def addons(self):
        return self.__addons

    @addons.setter
    def addons(self, addons):
        if not isinstance(addons, list):
            raise TypeError('ingredients must be of type list')
        if any(not isinstance(ingredient, str) for ingredient in addons):
            raise TypeError('ingredients must be of type str')
        self.__addons = addons

    def __str__(self):
        return f'Order: id={self.order_id}, customer={self.customer}, \n' \
               f'pizza={self.pizza},\n' \
               f'addons={self.addons}\n' \
               f'total-price={self.price}'
