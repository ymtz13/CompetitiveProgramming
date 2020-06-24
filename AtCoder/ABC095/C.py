A, B, C, X, Y = list(map(int, input().split()))
ans = 10**20
for nc in range(0, max(X,Y)*2+1, 2):
    na = max(X-nc//2, 0)
    nb = max(Y-nc//2, 0)
    ans = min(ans, na*A+nb*B+nc*C)
print(ans)
