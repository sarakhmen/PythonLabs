class Pizza:
    def __init__(self, name, price, ingredients=None):
        self.name = name
        self.price = price
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be of type str')
        self.__name = name

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
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, list):
            raise TypeError('ingredients must be of type list')
        if any(not isinstance(ingredient, str) for ingredient in value):
            raise TypeError('each ingredient must be of type str')
        self.__ingredients = value

