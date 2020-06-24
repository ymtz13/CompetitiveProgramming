N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))
xp = X[0]
ans = 0
for x in X[1:]:
    ans += min(A*(x-xp), B)
    xp = x
print(ans)
