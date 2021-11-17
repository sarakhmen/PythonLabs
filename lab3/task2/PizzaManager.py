from datetime import datetime

from SundayPizza import SundayPizza
from MondayPizza import MondayPizza
from TuesdayPizza import TuesdayPizza
from WednesdayPizza import WednesdayPizza
from ThursdayPizza import ThursdayPizza
from FridayPizza import FridayPizza
from SaturdayPizza import SaturdayPizza


class PizzaManager:
    addons = {'corn': 5,
              'quail eggs': 5,
              'marinated pork': 10
              }

    __pizzas = {'SundayPizza': SundayPizza('Curry', 150, ['tomato sauce', 'chicken curry', 'oregano']),
                'MondayPizza': MondayPizza('Mexicano', 140, ['bavarian salami', 'red onion', 'oregano']),
                'TuesdayPizza': TuesdayPizza('Pepperoni', 155, ['mozzarella cheese', 'bacon', 'tomato sauce']),
                'WednesdayPizza': WednesdayPizza('Diablo', 150, ['tomato sauce', 'fresh tomatoes', 'chorizo']),
                'ThursdayPizza': ThursdayPizza('Brasilia', 140, ['mozzarella cheese', 'bacon', 'sweet pepper']),
                'FridayPizza': FridayPizza('Fantasy', 160,
                                           ['mozzarella cheese', 'mascarpone cheese', 'parmesan cheese']),
                'SaturdayPizza': SaturdayPizza('Tonno', 150, ['mozzarella cheese', 'tuna', 'oregano'])
                }

    @staticmethod
    def get_pizza_of(pizza_name):
        return PizzaManager.__pizzas[pizza_name]

    @staticmethod
    def get_pizza_of_the_day():
        day = datetime.now().strftime("%A")
        for key in PizzaManager.__pizzas.keys():
            if day in key:
                return PizzaManager.__pizzas[key]
