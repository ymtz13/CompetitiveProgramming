N = int(input())
D = {}
for _ in range(N):
    s = input()
    if s not in D: D[s]=0
    D[s] += 1

M = int(input())
for _ in range(M):
    t = input()
    if t not in D: D[t]=0
    D[t] -= 1

print(max(D.values()))
