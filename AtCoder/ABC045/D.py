H, W, N = list(map(int, input().split()))
D = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    for dy in (-1, 0, +1):
        y = a + dy
        if y<=1 or y>=H: continue
        for dx in (-1, 0, +1):
            x = b + dx
            if x<=1 or x>=W: continue
            D.append((x,y))

D = sorted(D)

i = 0
M = len(D)
ans = [0]*10
while i<M:
    n = 1
    d = D[i]
    while i+n<M and D[i+n]==d: n+=1
    ans[n] += 1
    i+=n

ans[0] = (H-2)*(W-2) - sum(ans)
print(*ans, sep='\n')
