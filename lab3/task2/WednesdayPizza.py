from Pizza import Pizza


class WednesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Wednesday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'
