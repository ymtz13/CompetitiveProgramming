mod = 998244353

M2 = 70
M3 = 40
M5 = 30
M2M3 = M2 * M3
M = M2 * M3 * M5

N = int(input())

f2 = f3 = f5 = 0

while N % 2 == 0:
    f2 += 1
    N //= 2
while N % 3 == 0:
    f3 += 1
    N //= 3
while N % 5 == 0:
    f5 += 1
    N //= 5

if N > 1:
    print(0)
    exit()

dp = [0] * M
dp[0] = 1

f = pow(5, mod - 2, mod)
# f = 1 / 5

ans = 0

for _ in range(65):
    dp_next = [0] * M

    for n2 in range(M2 - 2):
        for n3 in range(M3 - 1):
            for n5 in range(M5 - 1):
                idx = n2 + M2 * n3 + M2M3 * n5
                v = dp[idx] * f % mod

                dp_next[idx + 1] += v
                dp_next[idx + M2] += v
                dp_next[idx + 2] += v
                dp_next[idx + M2M3] += v
                dp_next[idx + 1 + M2] += v

    dp = dp_next

    ans += dp[f2 + M2 * f3 + M2M3 * f5]
    ans %= mod

    # print(_)
    # for i, v in enumerate(dp):
    #     if v > 0:
    #         n2, n3, n5 = i % M3, (i % M2M3) // M3, i // M2M3
    #         print(pow(2, n2) * pow(3, n3) * pow(5, n5), (n2, n3, n5), v)

    # if _ > 5:
    #     break

print(ans)
