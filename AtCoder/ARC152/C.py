from math import gcd

N = int(input())
A = list(map(int, input().split()))

minA = min(A)
maxA = max(A)

G2 = minA + maxA
B = [a * 2 - G2 for a in A]

D = list(map(abs, B))
gcdD = D[0]
for d in D:
  gcdD = gcd(gcdD, d)

ans = minA % gcdD + (maxA - minA)

print(ans)
