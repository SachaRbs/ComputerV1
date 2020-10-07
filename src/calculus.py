from fractions import Fraction

def _sqrt(num):
  	return num**0.5

def solve_first_poly(polynome, fraction):
	x = - polynome[0] / polynome[1]
	if fraction:
		fraction = x.as_integer_ratio()
		print("The solution is: ")
		print("{}/{} = {}".format(fraction[0], fraction[1], x))
	else:
		print("The solution is:")
		print("{}".format(x))

def solve_second_poly(a, b, c, fraction):
	delta = (b**2) - (4 * a * c)
	if delta < 0:
		print("Discriminant is strictly negative, there is two complex solutions:")
		print("x1: ({} - i * √{})/{}".format(-b, -delta, 2 * a))
		print("x2: ({} + i * √{})/{}".format(-b, -delta, 2 * a))
		

	elif delta == 0:
		print("Discriminant is equal to zero the only solution is:")
		x = -b / (2 * a)
		if fraction:
			fraction = x.as_integer_ratio()
			print("x: {}/{} = {}".format(fraction[0], fraction[1], x))
		else:
			print("x: {}".format(x))
	else:
		print("Discriminant is strictly positive, the two solutions are:")
		x1 = (- b - _sqrt(delta)) / (2 * a)
		x2 = (-b + _sqrt(delta)) / (2 * a)
		if fraction:
			fraction1 = x1.as_integer_ratio()
			fraction2 = x2.as_integer_ratio()
			print("x1 : {}/{} = {}".format(fraction1[0], fraction1[1], x1))
			print("x2 : {}/{} = {}".format(fraction2[0], fraction2[1], x2))
		else:
			print("x1 :  {}".format(x1))
			print("x2 :  {}".format(x2))



def calculus(polynome, fraction):
	# print(polynome)
	if not polynome[0] and not polynome[1] and not polynome[2]:
		print(polynome)
		print("Reduced form: X = X")
		print("all the numbers are solution of the equation")
	elif not polynome[1] and not polynome[2]:
		print("There is no solution")
	elif polynome[2] == 0:
		solve_first_poly(polynome, fraction)
	else:
		solve_second_poly(polynome[2], polynome[1], polynome[0], fraction)





# $>./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
# Polynomial degree: 2
# Discriminant is strictly positive, the two solutions are:
# 0.905239
# -0.475131
# $>./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
# Reduced form: 1 * X^0 + 4 * X^1 = 0
# Polynomial degree: 1
# The solution is:
# -0.25
# ./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
# Polynomial degree: 3
# The polynomial degree is stricly greater than 2, I can't solve.