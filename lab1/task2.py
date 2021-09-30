import sys

operations = {"add": '+', "sub": '-', "div": '/', "mul": '*'}

if __name__ == '__main__':
    if len(sys.argv) != 4 or not sys.argv[2].isdigit() or not sys.argv[3].isdigit() or not sys.argv[1] in operations:
        print("Usage: (add | sub | div | mul) number number")
    else:
        try:
            result = eval(sys.argv[2] + " " + operations[sys.argv[1]] + " " + sys.argv[3])
            print("Your result = " + str(result))
        except ZeroDivisionError:
            print("Division by zero")

