import sympy as sym
from sympy.abc import x, y

# 다항식을 x로 미분
print(sym.diff(sym.poly(x**2 + 2*x +3), x))

# x로 편미분
# 왜 편미분을 사용할까?
# 벡터가 입력인 다변수 함수를 해석하기 위해서 사용한다.
print(sym.diff(sym.poly(x**2 + 2*x*y + 3) + sym.cos(x+2*y), x))