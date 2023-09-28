N = int(input())

ans = 0
for _ in range(N):
    A, T = map(int, input().split())
    ans = max(ans, max(A, T) + A)

print(ans)
