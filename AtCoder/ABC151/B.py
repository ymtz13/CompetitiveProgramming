N, K, M = list(map(int, input().split()))
S = sum(list(map(int, input().split())))
X = M*N-S
print(max(0,X) if X<=K else -1)
