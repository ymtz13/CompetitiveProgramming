import heapq

N, M, S = map(int, input().split())

E = [[] for _ in range(N)]
A = [[0]*N for _ in range(N)]
B = [[0]*N for _ in range(N)]
for i in range(M):
    U, V, a, b = map(int, input().split())
    u = U-1
    v = V-1
    E[u].append(v)
    E[v].append(u)
    A[u][v] = A[v][u] = a
    B[u][v] = B[v][u] = b

C = []
D = []
for i in range(N):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

M = 50*N
T = [[-1]*M for _ in range(N)]
h = []
heapq.heappush(h, (0, 0, min(M-1, S))) # (time, inode, snode)
while h:
    dmin, inode, snode = heapq.heappop(h)
    if T[inode][snode]!=-1: continue
    T[inode][snode] = dmin

    # (inode,snode) -> (enode, snode-a) with time b
    for enode in E[inode]:
        a = A[inode][enode]
        b = B[inode][enode]
        esnode = snode-a
        if esnode<0 or T[enode][esnode]!=-1: continue
        heapq.heappush(h, (dmin+b, enode, esnode))

    # (inode, snode) -> (inode, snode+c) with time d
    c = C[inode]
    d = D[inode]
    snode_c = min(M-1, snode+c)
    if T[inode][snode_c]!=-1: continue
    heapq.heappush(h, (dmin+d, inode, snode_c))

for inode in range(1, N):
    print(min([x for x in T[inode] if x>=0]))
    


    
    
    
