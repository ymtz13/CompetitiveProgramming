X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

PQ = [(p, 0) for p in P[:X]] + [(q, 1) for q in Q[:Y]]
PQ = sorted(PQ)

y = 0
for v, t in PQ:
    y += v

ans = y
r = 0
n = [X, Y]
for v, t in PQ:
    if n[t]==0: continue
    if r<C and v<R[r]:
       y += R[r]-v
       n[t] -= 1
       ans = max(ans, y)
       r += 1
       
print(ans)
