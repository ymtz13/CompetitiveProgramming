N, K = map(int, input().split())
A = list(map(int, input().split())) + [0] * 1000
ans = A[K:K + N]
print(' '.join(map(str, ans)))
