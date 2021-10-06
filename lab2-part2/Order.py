from Customer import Customer
from Product import Product


class Order:
    """
    This class represents an order entity

    """

    def __init__(self, customer, *products):
        self.customer = customer
        self.products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Products must be of Product type")
        self.__products = products

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of Customer type")
        self.__customer = customer

    def get_total_order_value(self):
        total_price = 0
        for product in self.products:
            total_price =+ product.price
        return total_price

