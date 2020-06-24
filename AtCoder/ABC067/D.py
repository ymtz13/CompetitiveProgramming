import sys
input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    E[a-1].append(b-1)
    E[b-1].append(a-1)

DF = [None]*N
DF[0] = 0
queue = [0]
while queue:
    queue_new = []
    for q in queue:
        for e in E[q]:
            if DF[e] is not None: continue
            DF[e] = DF[q]+1
            queue_new.append(e)
    queue = queue_new

DS = [None]*N
DS[N-1] = 0
queue = [N-1]
while queue:
    queue_new = []
    for q in queue:
        for e in E[q]:
            if DS[e] is not None: continue
            DS[e] = DS[q]+1
            queue_new.append(e)
    queue = queue_new
    
NF, NS = 0, 0
for df, ds in zip(DF,DS):
    if df<=ds: NF+=1
    else: NS+=1

print('Fennec' if NF>NS else 'Snuke')
