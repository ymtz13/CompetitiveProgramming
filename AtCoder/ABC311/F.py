mod = 998244353

H, W = map(int, input().split())
S = [input() for _ in range(H)]

T = []

prev = H + 1
for w in range(W):
    prev += 1
    hh = H
    for h in range(H):
        if h == prev:
            break
        if S[h][w] == "#":
            hh = prev = h
            break
    T.append(min(prev, hh))


dp = [0] * H
dp[0] = 1

w = W
for t in reversed(T):
    w -= 1

    # dp_next = [0] * H
    dp_next = dp[1:] + [0]
    dp_next[0] += dp[0]
    s = 0

    # for h in range(H):
    for h in range(t):
        if S[h][w] == "#":
            break

        s += dp[h]
        s %= mod

        dp_next[h] += s
        dp_next[h] %= mod

    dp = dp_next

ans = 0
for v in dp:
    ans += v
    ans %= mod

print(ans)
