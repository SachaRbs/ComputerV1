import re


def check_equation(equation):
	equation = equation.replace(' ', '')
	therms = re.split(r"\+|\-|\=", equation)
	therms = list(filter(None, therms))
	# print(therms)
	for therm in therms:
		if (re.search(r"[.?\d]+\*X\^[.?\d]+$", therm)) is None and therm != "0":
			print("ERROR: equation is not well formated, term [{}] is not formatted like [a * X^p]".format(therm))
			return False
	return True


def poly_zero(left, right):
	res = re.split(r"(\+|\-)", right)
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


def get_reduce(polynome):
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
	if reduce_ != "":
		reduce_ = (reduce_ + ' = 0').strip()
		print("Reduced form: {}".format(reduce_))
		print("Polynomial degree: {}".format(maxPol))
	return maxPol


def reduce_form(equation):
	if equation[0] != '+':
		equation = '+' + equation
	res = re.findall(r"[\+\-][.?\d]+\*X\^[.?\d]+", equation)
	polynome = {0: 0,
				1: 0,
				2: 0}
	for item in res:
		tmp = item.split('*')
		try:
			polynome[int(tmp[1][2:])] = polynome[int(tmp[1][2:])] + int_or_float(tmp[0])
		except:
			polynome[int(tmp[1][2:])] = int_or_float(tmp[0])
	maxPol = get_reduce(polynome)
	if maxPol > 2:
		return False
	return(polynome)