N, M = map(int, input().split())
S = []
for _ in range(M):
    A, B = map(int, input().split())
    S.append(max(0, N - A))

S.sort()
print(sum(S[:-1]))
