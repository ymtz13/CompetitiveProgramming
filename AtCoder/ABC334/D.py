N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

T = 10**6

S = []
s = 0
for r in R:
    s += r * T
    S.append(s)

for q in range(1, Q + 1):
    X = int(input())
    S.append(X * T + q)

S.sort()

ans = [None] * Q
a = 0
for v in S:
    t = v % T
    if t:
        ans[t - 1] = a
    else:
        a += 1

for a in ans:
    print(a)
