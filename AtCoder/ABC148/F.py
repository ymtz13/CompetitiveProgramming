import sys
input = sys.stdin.readline

N, u, v = list(map(int, input().split()))
E = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = list(map(int, input().split()))
    E[A-1].append(B-1)
    E[B-1].append(A-1)

#print(E)

parent = [None]*N
parent[v-1] = -1
depth = [None]*N
depth[v-1] = 0

queue = [v-1]
d=1
while queue:
    queue_new = []
    for q in queue:
        for e in E[q]:
            if parent[e] is not None: continue
            parent[e] = q
            queue_new.append(e)
            depth[e] = d

    queue = queue_new
    d+=1

#print(parent)
#print(depth)

w = u-1
x = (depth[u-1]-1)//2
for _ in range(x):
    w = parent[w]
    #print('rewind')

#print(w)

depth_from_w = 0
queue = [w]
while queue:
    queue_new = []
    for q in queue:
        for e in E[q]:
            if e==parent[q]: continue
            queue_new.append(e)

    queue = queue_new
    depth_from_w+=1

#print(depth_from_w-1)
print(depth[w] + depth_from_w-2)
