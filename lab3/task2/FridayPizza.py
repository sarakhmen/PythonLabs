from Pizza import Pizza


class FridayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Friday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'
