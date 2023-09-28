N = int(input())

L = []
S = 0
T = 0

for _ in range(N):
    X, Y, Z = map(int, input().split())
    S += Z

    if X > Y:
        T += Z
        continue

    H = (X + Y) // 2 + 1
    L.append((H - X, Z))

H = S // 2 + 1
if T >= H:
    print(0)
    exit()

R = H - T

# print(L, T, H, R)

dp = [1 << 60] * (S + 5)
dp[0] = 0
for cost, value in L:
    for i in range(S + 1, value - 1, -1):
        dp[i] = min(dp[i], dp[i - value] + cost)

    # print(dp)

print(min(dp[R:]))
