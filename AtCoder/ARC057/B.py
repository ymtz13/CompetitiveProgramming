N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

if K == sum(A):
    print(1)
    exit()

Sprev = A[0]
dp = [0, 1]
for a in A[1:]:
    S = Sprev + a
    dp_next = [0]
    for n in range(1, len(dp)):
        v = dp[n - 1] * S // Sprev + 1
        dp_next.append(min(dp[n], v if v <= S else 1 << 60))

    v = dp[-1] * S // Sprev + 1
    dp_next.append(v if v <= S else 1 << 60)

    Sprev = S
    dp = dp_next

for i, k in enumerate(dp):
    if k <= K:
        ans = i

print(ans)
