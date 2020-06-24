N = int(input())
D = {}
for _ in range(N):
    S = input()
    if S not in D: D[S]=0
    D[S]+=1

M = max(D.values())
for S in sorted(list(D)):
    if D[S]==M: print(S)
