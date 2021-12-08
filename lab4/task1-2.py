from datetime import date
from Person import Person
from Notebook import Notebook


def main():
    person1 = Person()
    person2 = Person('Artur', 'Sarakhman', '+380(97)-126-62-62', date(2001, 9, 15))
    notebook = Notebook(person1)
    notebook += person2
    notebook -= person1
    print(*(notebook*'Unknown'))
    print(*(notebook*'+380(97)-126-62-62'))


main()
