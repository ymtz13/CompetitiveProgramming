from random import randint

N = 100000
a = 999997
b = 999998
c = 999999

print(N, a, b, c)
print(*[randint(1, 10**3) for _ in range(N)])
