N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
D = {}
for a in A:
    if a not in D: D[a]=0
    D[a]+=1

print(sum(sorted(list(D.values()))[:-K]))
