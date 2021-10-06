class Product:
    """
    This class represents a product entity

    """
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("prise must be >= 0")
        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        self.__description = description

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, str):
            raise TypeError("Dimensions must be a string")
        self.__dimensions = dimensions

    def __str__(self):
        return f'Product [price = {self.price}, description = {self.description}, dimensions = {self.dimensions}]'
