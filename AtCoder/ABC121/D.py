A, B = list(map(int, input().split()))

def g(X):
    r = 1 if X&1 else X
    return r^1 if X&2 else r

print(g(A-1)^g(B))
