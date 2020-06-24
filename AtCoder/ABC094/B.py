N, M, X = list(map(int, input().split()))
nl = len([a for a in map(int, input().split()) if a<X])
print(min(nl,M-nl))
