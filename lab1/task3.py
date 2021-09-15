import sys

sign = ('+', '-')
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def is_formula_valid(formula, token):
    if len(formula) < 1 and token == "formula":
        return True
    if formula[0] in sign and token == "formula":
        return is_formula_valid(formula[1:], "number")
    elif formula[0] in number:
        return is_formula_valid(formula[1:], "formula")
    return False


if __name__ == '__main__':
    user_input = input("Your expression: ")
    if len(user_input) > 0 and is_formula_valid(user_input, "formula"):
        result = eval(user_input)
        print("True, " + str(result))
    else:
        print("False, None")
