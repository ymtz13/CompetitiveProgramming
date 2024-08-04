N = int(input())
X = list(map(int, input().split()))

n = 0
s = 0
ans = 0
for x in sorted(X):
    ans += x * n - s
    n += 1
    s += x

print(ans)
