mod = 998244353

N = int(input())
A = list(map(int, input().split()))

C = [0] * (201000)
# C = [0] * 6

for a in A:
    C[a] += 1

dp = [1]
for c in C:
    s = 0
    S = [0]
    for v in reversed(dp):
        s += v
        s %= mod
        S.append(s)
    S.reverse()

    dp_next = []
    for nop in range(N + 10):
        nop_prev = max(0, nop * 2 - c)
        v = S[min(nop_prev, len(S) - 1)]
        if v == 0:
            break
        dp_next.append(v)

    dp = dp_next
    # print(dp)

ans = 0
for v in dp:
    ans += v
    ans %= mod

print(ans)
