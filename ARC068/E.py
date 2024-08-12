N, M = map(int, input().split())
D = [0] * (M + 10)

for _ in range(N):
    L, R = map(int, input().split())
    D[L] += 1
    D[R + 1] -= 1

s = 0
S = []
for d in D:
    s += d
    S.append(s)

for m in range(1, M+1):
    for i in range(0, M+1, m):
        
