N = int(input())
X = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for x in X:
    s = sum(x[:4]) + x[4]*110/900
    ans = max(ans, s)

print(ans)
