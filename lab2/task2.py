from math import gcd


class Rational:
    """
    This class represents a rational number for performing arithmetic with fractions
    Parameters
    ----------
    numerator, denominator : 'int'
       fraction parts

    """

    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Wrong arguments!")
        if not denominator:
            raise ZeroDivisionError("Denominator cannot be 0")
        if not numerator:
            self.__numerator = 0
            self.__denominator = denominator
        else:
            divisor = gcd(numerator, denominator)
            self.__numerator = numerator // divisor
            self.__denominator = denominator // divisor

    def get_fraction(self):
        return f'{self.__numerator} / {self.__denominator}'

    def get_float(self):
        return self.__numerator / self.__denominator


if __name__ == '__main__':
    try:
        rational1 = Rational()
        print(rational1.get_fraction())
        print(rational1.get_float())

        rational2 = Rational(10, 20)
        print(rational2.get_fraction())
        print(rational2.get_float())

        rational3 = Rational(0, 10)
        print(rational3.get_fraction())
        print(rational3.get_float())
    except Exception as e:
        print(e)
