#Python lib
import sys
import re

#My lib
from utils import *
# from calculus import *

def parsing(equation):
    equation = equation.split('=')
    if (equation[1] != "0"):
        equation = poly_zero(equation[0], equation[1])
    else:
        equation = equation[0]
    therm = get_therm(equation)
    therm = extract(therm)
    return therm

def main():
    if len(sys.argv) == 2:
        therm = parsing(sys.argv[1].replace(' ', ''))
        # calculus(therm)
    else:
        print('ERROR Usage : python3 computer.py "some polynomial function')

if __name__ == "__main__":
    main()