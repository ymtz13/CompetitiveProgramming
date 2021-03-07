N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(K)]

mod = 998244353

S = [0, 1]

for i in range(2, N+1):
    a = 0
    for l, r in LR:
        a = (a + S[max(i-l, 0)]-S[max(i-r-1,0)]) % mod
    S.append((S[-1] + a) % mod)

print(a)
