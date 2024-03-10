mod = 998244353

N = int(input())
A = list(map(int, input().split()))

dp = [1]
p = [0] * (N + 1)
P = [None]

s = 0
S = [0]

for i, a in enumerate(A, 1):
    X = tuple(range(1, N + 1)) if a == -1 else [a]
    v = dp[-1] * len(X) % mod
    print((i, a), v)
    for x in X:
        px = p[x]
        l = i - px

        if l > x:
            # c = S[i - x - 1] - S[px]
            # v -= dp[px] * pow(N, c, mod) % mod
            v -= dp[i - x - 1]
            v %= mod
            # print(px, l, x, c, v)
            print(px, l, x, v)

    dp.append(v)

    if a == -1:
        s += 1
    else:
        for b in range(N + 1):
            if b != a:
                p[b] = i

    P.append(p[:])
    S.append(s)


print(dp)
print(dp[-1] % mod)

# for p in P:
#     print(p)
# print("S:", S)
