N, K, S = map(int, input().split())

a = 1 if S==10**9 else S+1
A = [S]*K + [a] * (N-K)
print(*A)
