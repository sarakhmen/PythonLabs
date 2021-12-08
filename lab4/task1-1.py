from Rational import Rational


def main():
    rational1 = Rational(1, 2)
    rational2 = Rational(3, 4)
    print(rational1 == rational2)
    print(rational1 != rational2)
    print(rational1 + rational2)
    print(rational1 - rational2)
    print(rational1 / rational2)
    print(rational1 * rational2)
    rational1 += rational2
    print(rational1)
    rational1 -= rational2
    print(rational1)
    rational1 *= rational2
    print(rational1)
    rational1 /= rational2
    print(rational1)
    try:
        rational3 = Rational(1, 0)
    except Exception as e:
        print(e)


main()

