from scipy.optimize import linprog

N = int(input())
C1 = []
C2 = []

for _ in range(N):
  A, B, C = map(int, input().split())
  C1.append(A / C)
  C2.append(B / C)

c = [-1] * N
A = [C1, C2]
res = linprog(c, A_ub=A, b_ub=[1] * 2, bounds=((0, None), ) * N)
print(-res.fun)
