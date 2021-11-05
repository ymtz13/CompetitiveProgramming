N = int(input())
p = []
for i in range(N):
    x, y = [int(c) for c in input().split()]
    p.append((x,y))

t = {}
for i, pi in enumerate(p):
    for j, pj in enumerate(p):
        if i==j : continue
        
        dx, dy = pi[0] - pj[0], pi[1] - pj[1]
        if (dx, dy) in t:
            t[(dx, dy)] += 1
        else:
            t[(dx, dy)] = 1

if N==1:
    print(1)
else:
    print(N-max([t[k] for k in t]))
