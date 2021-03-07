X, K, D = map(int, input().split())
X = abs(X)

N = X//D
if K<=N:
    ans = X-K*D
else:
    K -= N
    X = X%D
    ans = D-X if K&1 else X
print(ans)
