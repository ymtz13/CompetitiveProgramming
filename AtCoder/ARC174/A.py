N, C = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)

D = [a * C - a for a in A]

z = 0
s = 0
smin = 0
for d in D:
    s += d

    z = max(z, s - smin)
    smin = min(smin, s)

print(S + z)
