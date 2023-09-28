N, X, Y = map(int, input().split())
PT = [map(int, input().split()) for _ in range(N - 1)]

Q = int(input())
Queries = [int(input()) for _ in range(Q)]

S = list(range(840))
for P, T in PT:
    Pm1 = P - 1
    S = [T + ((v + Pm1) // P) * P for v in S]


S = [v - i for i, v in enumerate(S)]

ans = []
for q in Queries:
    d = q + X
    t = d + S[d % 840] + Y
    ans.append(t)

for a in ans:
    print(a)
