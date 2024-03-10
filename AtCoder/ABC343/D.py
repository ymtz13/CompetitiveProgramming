from collections import defaultdict

N, T = map(int, input().split())

D = defaultdict(int)
D[0] = N
S = {0}
P = [0] * (N + 1)

ans = []
for _ in range(T):
    A, B = map(int, input().split())

    p = P[A]
    D[p] -= 1
    if D[p] == 0:
        S.remove(p)

    q = p + B
    P[A] = q
    D[q] += 1
    S.add(q)

    ans.append(len(S))

for a in ans:
    print(a)
