import re
from itertools import groupby 

def poly_zero(left, right):
    """Function that return the equation with all the termes 
        at the right of the equation and 0 at the left"""
    item = re.split('(\+|\-)', right)
    inverse = {"+": "-", "-": "+"}
    get = '+'
    for i in item:
        if i == "+" or i == "-":
            get = i
            continue
        left = left + inverse[get] + i
        get = "+"
    return left

def get_therm(equation):
    tmp = re.split('(\+|\-)', equation)
    get = ""
    therm = []
    for i in tmp:
        if i == "+" or i == "-":
            if i == "-":
                get = i
            continue
        therm.append(get + i)
        get = ""
    therm.sort()
    res = [list(i) for j, i in groupby(therm,
           lambda a: a[a.find('^') + 1])]
    # print(res)
    return res

def extract(therm):
    print(therm)
    polynome = {0: 0, #what if X^3
                1: 0,
                2: 0}
    for item in therm:
        for i in range(0, len(item)):
            tmp = item[i].split('*')
            if int(tmp[1][-1]) > 2 or int(tmp[1][-1]) < 0:
                print("-------ERROR----------")
            polynome[int(tmp[1][-1])] =  polynome[int(tmp[1][-1])] + float(tmp[0])
    # print("Reduced form: {} * X^0 + {} * X^1 {} * X^2 = 0")
    return(polynome)
