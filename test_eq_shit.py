from sympy import symbols
import sympy as sy
x, y = symbols('x y')
expr = x/-3 + y/4
expr_ = sy.Eq(expr, 1)

print(expr_)
print(expr_.subs(x, 2))