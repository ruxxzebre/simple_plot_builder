# импортируем модули
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
import sympy as sy
import time

#ex = 'y/4 + x/-3'
#res = float(1)
#
def solver(ex):
    ex = ex.split('=')
    if (ex[1] != '0'):
        res = float(ex[1])
    else:
        res = 0

    ex = ex[0].strip()

    x, y = symbols('x y')
    expr =  sy.Eq(sy.sympify(ex))
    express = sy.lambdify(x, sy.solve(expr, y)[0])
    y = express

    flag = True
    if flag:
        # создаём рисунок с координатную плоскость
        fig = plt.subplots()
        # создаём область, в которой будет
        # - отображаться график
        x = np.linspace(-3, 3,100)
        # значения x, которые будут отображены
        # количество элементов в созданном массиве
        # - качество прорисовки графика 
        # рисуем график
        plt.plot(x, y(x))
        # показываем график
        plt.show()

def close():
    plt.close()

