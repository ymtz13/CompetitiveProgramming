N, M, P = map(int, input().split())

ans = 0
for d in range(1, N + 1):
    if d >= M and (d - M) % P == 0:
        ans += 1

print(ans)
