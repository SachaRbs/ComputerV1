
def _sqrt(num):
  	return num**0.5

def solve_first_poly(polynome):
    res = - polynome[0] / polynome[1]
    print("The solution is:")
    print(res)

def solve_second_poly(a, b, c):
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print("Discriminant is strictly negative, there is no solution:")
        print("pas de solution")
    elif delta == 0:
        print("Discriminant is equal to zero the only solution is:")
        x = -b / (2 * a)
        print("une solution : {}".format(res))
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        x1 = (- b - _sqrt(delta)) / (2 * a)
        x2 = (-b + _sqrt(delta)) / (2 * a)
        print("x1 : {}".format(x1))
        print("x2 : {}".format(x2))



def calculus(polynome):
    # print(polynome)
    if not polynome[1] and not polynome[2]:
        print("tout les nombres sont solutions")
    elif polynome[2] == 0:
        solve_first_poly(polynome)
    else:
        solve_second_poly(polynome[2], polynome[1], polynome[0])





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