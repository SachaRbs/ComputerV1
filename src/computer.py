#Python lib
import sys
import re

def check_equation(equation):
    equation = equation.replace(' ', '')
    therms = re.split("\+|\-|\=", equation)
    therms = list(filter(None, therms))
    # print(therms)
    for therm in therms:
        if (re.search("[.?\d]+\*X\^[0-2]$", therm)) is None:
            return False
    return True

def poly_zero(left, right):
    res = re.split("(\+|\-)", right)
    res = list(filter(None, res))
    get = '+'
    inverse = {'-': '+', '+': '-'}
    multi = 0
    for item in res:
        if item == '-' or item =='+':
            if item == '-':
                get = '-'
            multi = multi + 1
            if multi == 2:
                print("Error")
                return False
            continue
        multi = 0
        left = left + inverse[get] + item
        get = '+'
    print(left)
    return left

def reduce_form(equation):
    res = re.findall("[\+\-][.?\d]+\*X\^[.?\d]+", equation)
    polynome = {0: 0,
                1: 0,
                2: 0}
    for item in res:
        tmp = item.split('*')
        print(tmp)
        polynome[int(tmp[1][-1])] = polynome[int(tmp[1][-1])] + float(tmp[0])
    print(polynome)

    return equation

def parsing(equation):
    if check_equation(equation) is False:
        print("ERROR")
        return False
    equation = equation.split('=')
    if len(equation) != 2:
        return(False)
    if (equation[0] != "0") or (equation[1] != "0"):
        equation = poly_zero(equation[0], equation[1])
    elif equation[0] == "0":
        equation = equation[1]
    elif equation[1] == "0":
        equation = equation[0]
    if equation == False:
        print("ERROR")
        exit()
    equation = reduce_form(equation)
    return

def main():

    if len(sys.argv) == 2:
        parsing(sys.argv[1].replace(' ', ''))


if __name__ == "__main__":
    main()

    import re


# equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 =  -1 * X^20"
# if checkEquation(equation) is False:
#     print("error")
#     exit()
# if equation[0] != '+' or equation[0] != '-':
#     equation = '+' + equation

# equation = equation.replace(' ', '')
