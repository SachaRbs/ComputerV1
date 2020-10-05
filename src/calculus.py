from math import sqrt

def solve_first_poly(polynome):
    res = - polynome[0] / polynome[1]
    print(res)

def solve_second_poly(a, b, c):
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print("discriminant = {} < 0".format(delta))
        print("pas de solution")
    elif delta == 0:
        print("discriminant = {} = 0".format(delta))
        x = -b / (2 * a)
        print("une solution : {}".format(res))
    else:
        print("discriminant = {} > 0".format(delta))
        x1 = (- b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("x1 : {}".format(x1))
        print("x2 : {}".format(x2))



def calculus(polynome):
    # print(polynome)
    if polynome[1] == 0 and polynome[2] == 0:
        print("tout les nombres sont solutions")
    elif polynome[2] == 0:
        solve_first_poly(polynome)
    else:
        solve_second_poly(polynome[2], polynome[1], polynome[0])