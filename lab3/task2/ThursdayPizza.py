from Pizza import Pizza


class ThursdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def __str__(self):
        return f'Thursday pizza: {self.name}, price: {self.price}, ingredients: {self.ingredients}'
