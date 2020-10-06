#Python lib
import sys
import re

from calculus import *

def check_equation(equation):
    equation = equation.replace(' ', '')
    therms = re.split("\+|\-|\=", equation)
    therms = list(filter(None, therms))
    # print(therms)
    for therm in therms:
        if (re.search("[.?\d]+\*X\^[0-9]$", therm)) is None:
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
    return left

def int_or_float(s):
    try:
        return int(s)
    except:
        return float(s)

def reduce_form(equation):
    if equation[0] != '+':
        equation = '+' + equation
    res = re.findall("[\+\-][.?\d]+\*X\^[.?\d]+", equation)
    polynome = {0: 0,
                1: 0,
                2: 0}
    for item in res:
        tmp = item.split('*')
        try:
            polynome[int(tmp[1][-1])] = polynome[int(tmp[1][-1])] + int_or_float(tmp[0])
        except:
            polynome[int(tmp[1][-1])] = int_or_float(tmp[0])
    reduce_ = ""
    sign = ""
    maxPol = 0
    for i in polynome:
        if polynome[i] != 0:
            maxPol = i
            if polynome[i] < 0:
                sign = ' - '
                reduce_ = reduce_ + sign + '{} * X^{}'.format((polynome[i] * -1), i)
            elif polynome[i] == 0:
                reduce_ = reduce_ + sign + 'X^{}'.format(i)
            else:
                reduce_ = reduce_ + sign + '{} * X^{}'.format(polynome[i], i)
            sign = ' + '
    reduce_ = (reduce_ + ' = 0').strip()
    print("Reduced form: {}".format(reduce_))
    print("Polynomial degree: {}".format(maxPol))
    if maxPol > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        return False
    return(polynome)


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
    polynome = reduce_form(equation)
    return polynome

def main():
    if len(sys.argv) == 2:
        polynome = parsing(sys.argv[1].replace(' ', ''))
        if polynome is not False:
            calculus(polynome)


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
