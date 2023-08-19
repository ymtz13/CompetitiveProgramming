N, M = map(int, input().split())

ans = INF = 1 << 60
for a in range(1, 1000010):
    if a > N:
        break

    b = (M + a - 1) // a
    if b <= N:
        ans = min(ans, a * b)

print(ans if ans < INF else -1)
