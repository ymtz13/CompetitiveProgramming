from bisect import bisect

N, M = map(int, input().split())
X = [1]*N

A = map(int, input().split())
for a in A:
    i = bisect(X,-a)
    if i<N:
        X[i] = -a
        print(i+1)
    else:
        print(-1)
    
