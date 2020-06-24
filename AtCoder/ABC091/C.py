N = int(input())
R = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

M = 2*N+2
s = 2*N
g = 2*N+1
E = [[False]*M for _ in range(M)]

for ir, (rx, ry) in enumerate(R):
    for ib, (bx, by) in enumerate(B):
        if rx<bx and ry<by:
           E[ir][ib+N] = True

for i in range(N):
    E[s][i] = True
    E[i+N][g] = True

while True:
    K = [None]*M
    K[s] = -1
    queue = [s]
    while queue and (K[g] is None):
        queue_new = []
        for q in queue:
            for e, f in enumerate(E[q]):
                if not f: continue
                if K[e] is not None: continue
                K[e] = q
                queue_new.append(e)

        queue = queue_new

    #print(K)
    #input("aa")

    if K[g] is None:
        break
    else:
        i = g
        while K[i]!=-1:
            #print(i,end=' ')
            E[K[i]][i] = False
            E[i][K[i]] = True
            i = K[i]

ans = 0
for ir in range(N):
    if not E[s][ir]: ans += 1
print(ans)

