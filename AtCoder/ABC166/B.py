N, K = map(int, input().split())
S = set()
for k in range(K):
    input()
    S |= set(map(int, input().split()))
print(N-len(S))
