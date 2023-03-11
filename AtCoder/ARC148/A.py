from math import gcd

N = int(input())
A = list(map(int, input().split()))

a0 = A[0]
D = [a - a0 for a in A]

gcdD = 0
for d in D:
  gcdD = gcd(gcdD, d)

print(2 if gcdD == 1 else 1)
