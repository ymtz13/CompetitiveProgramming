N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]
Smax = max(S)
Smin = min(S)
Savg = sum(S)/N

D = Smax-Smin
if D==0:
    print(-1)
    exit()

P = B/D
Q = A - Savg*P
print(P, Q)