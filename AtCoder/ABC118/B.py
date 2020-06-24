N, M = list(map(int, input().split()))
L = [0]*M
for n in range(N):
    KA = list(map(int, input().split()))
    for a in KA[1:]:
        L[a-1]+=1

print(L.count(N))
