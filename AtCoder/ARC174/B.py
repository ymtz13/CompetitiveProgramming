def solve(A, P):
    X = -sum([a * i for i, a in enumerate(A, -2)])
    if X <= 0:
        return 0

    P4, P5 = P[3:]

    C44 = X * P4
    C55 = ((X + 1) // 2) * P5
    C45 = (X // 2) * P5 + P4
    return min(C44, C55, C45)


T = int(input())
ans = []
for _ in range(T):
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))

    a = solve(A, P)
    ans.append(a)

for a in ans:
    print(a)
