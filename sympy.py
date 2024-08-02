import sympy as sm
a,b= sm.symbols("a b")
expr = (a + b) ** 2
print(sm.expand(expr))