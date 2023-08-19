mod = 998244353

N = int(input())
T = input()

offset = N + 2
N2 = (N * 2) + 5
dp = [0] * N2
dp[0 + offset] = 1

np = T.count("+")
nm = T.count("-")
nq = T.count("?")
ex = 0

for k, c in enumerate(T, 1):
    dp_next = [0] * N2

    if c == "+":
        np -= 1
    if c == "-":
        nm -= 1
    if c == "?":
        nq -= 1

    if c != "-":
        for i in range(1, N2):
            idx = i - offset
            if idx > nm + nq - np:
                break
            dp_next[i] += dp[i - 1]
            v = dp[i - 1] * min(abs(idx), abs(idx - 1))
            if v:
                print(k, idx, ":", dp[i - 1], min(abs(idx), abs(idx - 1)), v)
            ex += v

    if c != "+":
        for i in range(N2 - 2, -1, -1):
            idx = i - offset
            if -idx > np + nq - nm:
                break
            dp_next[i] += dp[i + 1]

            v = dp[i + 1] * min(abs(idx), abs(idx + 1))
            if v:
                print(k, idx, ":", dp[i + 1], min(abs(idx), abs(idx + 1)), v)
            ex += v

    dp = dp_next
    print(dp)

base = dp[0 + offset] * N
print(base)
print(ex)

print((base + ex) % mod)
