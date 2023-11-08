N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

C = [[] for _ in range(N + 1)]
S = [-(1 << 60)] * (N + 1)

for i, (s, a) in enumerate(reversed(P)):
    i = N - i
    C[s].append(i)
    s = a + sum([max(0, S[c]) for c in C[i]])
    S[i] = s

print(max(S))
