N = int(input())
V = list(map(int, input().split()))

d1 = {0:0}
d2 = {0:0}
for i, v in enumerate(V):
    d = d2 if i&1 else d1
    if v not in d: d[v]=0
    d[v]+=1
    

d1 = sorted(list(d1.items()), key=lambda x:-x[1])
d2 = sorted(list(d2.items()), key=lambda x:-x[1])

if d1[0][0]!=d2[0][0]:
    print(N-d1[0][1]-d2[0][1])
else:
    print(min(N-d1[1][1]-d2[0][1], N-d1[0][1]-d2[1][1]))
