mod = 10007

N = int(input())
S = [1 << ("JOI".index(c)) for c in input()]

dp = [0] * 8
dp[0b001] = 1

for c in S:
    dp_next = [0] * 8

    for curr in range(8):
        if not curr & c:
            continue

        s = 0
        for prev in range(8):
            if prev & curr:
                s += dp[prev]

        dp_next[curr] = s % mod

    dp = dp_next

print(sum(dp) % mod)
