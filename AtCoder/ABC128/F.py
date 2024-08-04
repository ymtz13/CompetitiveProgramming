N = int(input())
S = list(map(int, input().split()))

ans = 0
for D in range(1, N // 2):
    s = set()
    t = 0
    for L in range(D, N - 1, D):
        R = N - 1 - L
        if L in s:
            break
        s.add(L)

        if R in s or R < D:
            break
        s.add(R)

        t += S[L] + S[R]

        # print(D, s, t)
        ans = max(ans, t)


print(ans)
