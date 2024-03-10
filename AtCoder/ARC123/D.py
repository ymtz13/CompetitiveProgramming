N = int(input())
A = list(map(int, input().split()))

vInc = A[0]
vDec = 0

Inc = [vInc]
Dec = [vDec]

for p, a in zip(A, A[1:]):
    d = a - p
    if a > 0:
        vInc += d
    else:
        vDec += d
    Inc.append(vInc)
    Dec.append(vDec)


V = Inc + [-v for v in Dec]
V.sort()

c = V[N]

ans = 0
for v in V:
    ans += abs(v - c)

print(Inc)
print(Dec)
print(V)
print(c)

print([v - c for v in Inc])
print([v + c for v in Dec])

print(ans)
