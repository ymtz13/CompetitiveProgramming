from bisect import bisect_left

N, M = map(int, input().split())
ST = [tuple(map(int, input().split())) for _ in range(M)]

D = [0]*(N+1)
for s,t in ST:
    D[s-1] += 1
    D[t] -= 1

X = []
x = 0
for d in D[:-1]:
    x += d
    X.append(x)

Z = [i for i, x in enumerate(X) if x==1] + [N+100]
    
ans = [m+1 for m, (s, t) in enumerate(ST) if Z[bisect_left(Z, s-1)]>=t ]

print(len(ans))
if ans: print('\n'.join(map(str, ans)))
