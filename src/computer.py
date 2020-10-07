#Python lib
import sys
import re

from calculus import *
from utils import *


def parsing(equation):
	if check_equation(equation) is False:
		exit()
	equation = equation.split('=')
	if len(equation) != 2:
		print("ERROR: equation is not well formatted, it has to be an equality with only one ('=')")
		exit()
	if equation[0] == "" or equation[1] == "":
		print("ERROR: Missing one side of the equality")
		exit()
	if (equation[0] != "0") or (equation[1] != "0"):
		equation = poly_zero(equation[0], equation[1])
		if equation == False:
			print("ERROR: equation is not well formatted")
			exit()
	elif equation[0] == "0":
		equation = equation[1]
	elif equation[1] == "0":
		equation = equation[0]
	if equation:
		polynome = reduce_form(equation)
	else:
		print("ERROR: Equation does not exist")
		exit()
	if polynome is False:
		print("The polynomial degree is stricly greater than 2, I can't solve.")
		exit()
	return polynome


def input_polynome():
	print("equation is of the type : a * X^2 + b * X^1 + c * X^0")
	polynome = {}
	a = input("a = ? ")
	try:
		a = float(a)
	except:
		print("ERROR input has to be a number")
		exit()
	b = input("b = ? ")
	try:
		b = float(b)
	except:
		print("ERROR input has to be a number")
		exit()
	c = input("c = ? ")
	try:
		c = float(c)
	except:
		print("ERROR input has to be a number")
		exit()
	polynome[2] = a
	polynome[1] = b
	polynome[0] = c
	get_reduce(polynome)
	return(polynome)


def main():
	fraction = 0
	if len(sys.argv) >= 2:
		if len(sys.argv) > 2 and sys.argv[2] == "-F":
			fraction = 1
		polynome = parsing(sys.argv[1].replace(' ', ''))
		if polynome is not False:
			calculus(polynome, fraction)
	else:
		print("Usage: python3 computer.py '[POLYNOME]'")
		print("OPTION: -F : Write solution into a fraction")
		r = input("do you want to create a polynome ? [y/n]")
		if r == 'y':
			polynome = input_polynome()
			calculus(polynome, 0)


if __name__ == "__main__":
	main()
