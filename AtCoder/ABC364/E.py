import numpy as np
from scipy.optimize import milp
from scipy.optimize import LinearConstraint
from scipy.optimize import Bounds

N, X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

c = np.array([-1] * N)
A = np.array(AB).T
b_u = np.array([X, Y])
b_l = np.array([0, 0])
l = np.array([0] * N)
u = np.array([1] * N)
bounds = Bounds(l, u)
constraints = LinearConstraint(A, b_l, b_u)
integrality = np.array([1] * N)

# print(c)
# print(A)
# print(b_u)
# print(b_l)
# print(constraints)

res = milp(
    c=c,
    bounds=bounds,
    constraints=constraints,
    integrality=integrality,
)
# print(res)
print(min(N, 1 + int(-res.fun + 0.1)))
