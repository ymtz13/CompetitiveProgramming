from collections import defaultdict

N, P = map(int, input().split())
A = list(map(int, input().split()))

Q = P - 1
D = set()

for i in range(1, Q + 1):
    if i * i > Q:
        break

    if Q % i == 0:
        D.add(i)
        D.add(Q // i)

D = sorted(list(D))

B = []
C = defaultdict(int)
for a in A:
    for d in D:
        if pow(a, d, P) == 1:
            x = Q // d
            B.append(x)
            C[x] += 1
            break

# print(B)

ans = 0
for x, cx in C.items():
    for y, cy in C.items():
        if y % x == 0:
            ans += cx * cy

print(ans)
