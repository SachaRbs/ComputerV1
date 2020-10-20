import matplotlib.pyplot as plt
import numpy as np

def verbose(a, b, c):
	print('------------VERBOSE------------')
	delta = (b**2) - (4 * a * c)
	print('\u0394 = b\u00B2 - 4ac')
	print('\u0394 = {}\u00B2 - 4 * {} * {}'.format(b, a, c))
	print('\u0394 = {}'.format(delta))
	print()
	if delta > 0:
		print('\u0394 > 0')
		print()
		print('x1 = (-b - \u221a\u0394) / 2a')
		print('x2 = (-b + \u221a\u0394) / 2a')
		print()
		print('x1 = ({} - \u221a{}) / {}'.format(-b, delta, 2 * a))
		print('x2 = ({} + \u221a{}) / {}'.format(-b, delta, 2 * a))
	elif delta == 0:
		print('\u0394 == 0')
		print()
		print("x = -b / 2a")
		print("x = {} / {}".format(-b, 2 * a))
	else:
		print('\u0394 < 0')
		print('\u0394 = (ir)\u00B2')
		print()
		print('z1 = (-b + ir) / 2a')
		print('z2 = (-b + ir) / 2a')
	print('-------------------------------')

	

def _sqrt(num):
  	return num**0.5

def solve_first_poly(polynome, args):
	x = - polynome[0] / polynome[1]
	if args.fraction:
		fraction = x.as_integer_ratio()
		print("The solution is: ")
		print("{}/{} = {}".format(fraction[0], fraction[1], x))
	else:
		print("The solution is:")
		print("{}".format(x))

def solve_second_poly(a, b, c, args):
	delta = (b**2) - (4 * a * c)
	if args.verbose:
		verbose(a, b, c)
	if delta < 0:
		print("Discriminant is strictly negative, there is two complex solutions:")
		print("z1: ({} - i * √{})/{}".format(-b, -delta, 2 * a))
		print("z2: ({} + i * √{})/{}".format(-b, -delta, 2 * a))

	elif delta == 0:
		print("Discriminant is equal to zero the only solution is:")
		x = -b / (2 * a)
		if args.fraction:
			fraction = x.as_integer_ratio()
			print("x: {}/{} = {}".format(fraction[0], fraction[1], x))
		else:
			print("x: {}".format(x))
	else:
		print("Discriminant is strictly positive, the two solutions are:")
		x1 = (- b - _sqrt(delta)) / (2 * a)
		x2 = (-b + _sqrt(delta)) / (2 * a)
		if args.fraction:
			fraction1 = x1.as_integer_ratio()
			fraction2 = x2.as_integer_ratio()
			print("x1 : {}/{} = {}".format(fraction1[0], fraction1[1], x1))
			print("x2 : {}/{} = {}".format(fraction2[0], fraction2[1], x2))
		else:
			print("x1 :  {}".format(x1))
			print("x2 :  {}".format(x2))

def trinome(a,b,c,x):
    return (a*x**2 + b*x + c)

def plot_graph(a,b,c):
    x = np.linspace(-10,10,100)
    
    plt.plot(x,trinome(a,b,c, x))

    plt.axvline(x=0, color ='r')
    plt.axhline(y=0, color ='r')   
    axes = plt.gca()
    axes.set_xlabel('x : abscisse')
    axes.set_ylabel('f(x) : ordonnée')

    plt.show()

def calculus(polynome, args):
	if not polynome[0] and not polynome[1] and not polynome[2]:
		print(polynome)
		print("Reduced form: X = X")
		print("all the numbers are solution of the equation")
		exit()
	elif not polynome[1] and not polynome[2]:
		print("There is no solution")
		exit()
	elif polynome[2] == 0:
		solve_first_poly(polynome, args)
	else:
		solve_second_poly(polynome[2], polynome[1], polynome[0], args)
	if args.graph:
		plot_graph(polynome[2], polynome[1], polynome[0])