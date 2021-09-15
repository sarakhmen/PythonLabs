import sys

operations = ('+', '-', '/', '*')

if __name__ == '__main__':
    if len(sys.argv) != 4 or not sys.argv[1].isdigit() or not sys.argv[3].isdigit() or not sys.argv[2] in operations:
        print("Usage: number [+ | - | / | *) number")
    else:
        result = eval(sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])
        print("Your result = " + str(result))
