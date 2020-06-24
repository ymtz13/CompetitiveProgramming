N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
o = (min(P, key=lambda p:p[0])-1, min(P, key=lambda p:p[1])-1)

for p in P:
    dx, dy = p[0]-o[0], p[1]-o[1]
    
