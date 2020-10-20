import argparse
import sys
import re

from calculus import *
from utils import *


def parsing(equation):
	if check_equation(equation) is False:
		exit()
	equation = equation.split('=')
	if len(equation) != 2:
		print("ERROR: Equation is not well formatted, it has to be an equality with only one ('=')")
		exit()
	if equation[0] == "" or equation[1] == "":
		print("ERROR: Missing one side of the equality")
		exit()
	if (equation[0] != "0") or (equation[1] != "0"):
		equation = poly_zero(equation[0], equation[1])
		if equation == False:
			print("ERROR: Equation is not well formatted")
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

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("equation", help="polynomial equation to solve")
	parser.add_argument("-f", "--fraction", help="print the result of the equation as a fraction", action="store_true")
	parser.add_argument("-g", "--graph", help="plot the graph of the polynome", action="store_true")
	parser.add_argument("-v", "--verbose", help="calculs details", action="store_true")

	args = parser.parse_args()
	polynome = parsing(args.equation.replace(' ', ''))
	print(args.fraction)
	if polynome is not False:
		calculus(polynome, args)

if __name__ == "__main__":
	main()
