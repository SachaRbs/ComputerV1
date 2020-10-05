import re
from itertools import groupby

def checkEquation(equation):
	reg = re.compile('[0-9X\s\^\-\+\*\=\.\/]+$')
	const = re.search('(?<=[^X])\^', equation)
	const2 = re.search('\^(?![0-2])', equation)
	const3 = re.search('(?<=\d)\s(?=\d)', equation)

	if not reg.match(equation):
		print('Wrong caracters in equation.')
		return False
	if const is not None or const2 is not None or const3 is not None:
		print('Polynome not well formatted.')
		return False
	return True


def poly_zero(left, right):
    res = re.split("(\+|\-)", right)
    if res[0] == '':
        res = res[1:]
    print(res)