from math import pi
N = int(input())
R2 = sorted([int(input())**2 for _ in range(N)], reverse=True)
print(pi*(sum(R2[::2])-sum(R2[1::2])))

