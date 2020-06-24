H, W = map(int, input().split())
M = [[-1]*(W+2) for _ in range(H+2)]
X = []
for h in range(H):
    for w, c in enumerate(input()):
        if c=='.':
            M[h+1][w+1] = 0
            X.append((h+1, w+1))

from pprint import pprint
pprint(M)

mark = 0
ans = 0
for ist, st in enumerate(X):
    for gl in X[ist+1:]:
        mark += 1
        turn = 0
        f = False
        queue = [st]
        while queue and not f:
            queue_new = []
            for qx, qy in queue:
                if (qx, qy)==gl:
                    f = True
                    break
                    
                for dx, dy in ((+1,0),(-1,0),(0,+1),(0,-1)):
                    x = qx+dx
                    y = qy+dy
                    m = M[x][y] 
                    if m!=-1 and m!=mark:
                        M[x][y] = mark
                        queue_new.append((x,y))
                        
            
            queue = queue_new
            turn += 1

        ans = max(ans, turn-1)

print(ans)
