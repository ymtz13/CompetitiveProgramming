import heapq

H, W = map(int, input().split())
C = []
C.append('X'*(W+2))
for h in range(H):
    C.append('X{}X'.format(input()))
C.append('X'*(W+2))

for h in range(1, H+1):
    for w in range(1, W+1):
        if C[h][w]=='s': sh, sw = h, w
        if C[h][w]=='g': gh, gw = h, w

X = [[-1]*(W+2) for _ in range(H+2)]
        
Q = [(0, sh, sw)]
while Q:
    c, h, w = heapq.heappop(Q)
    if C[h][w]=='X' or X[h][w]!=-1: continue
    X[h][w]=c

    for dh, dw in [(+1,0),(-1,0),(0,+1),(0,-1)]:
        hh = h+dh
        ww = w+dw
        cc = c+1 if C[hh][ww]=='#' else c
        heapq.heappush(Q, (cc ,hh, ww))

print('YES' if X[gh][gw]<=2 else 'NO')
