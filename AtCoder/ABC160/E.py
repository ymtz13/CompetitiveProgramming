X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

p = X # num of red 
r = 0 # num of noncolor
while p>0 and r<C and P[p-1]<R[r]:
    p -= 1
    r += 1

q = Y # num of green
while q>0 and r<C and Q[q-1]<R[r]:
    q -= 1
    r += 1

ans = y = sum(P[:p]) + sum(Q[:q]) + sum(R[:r])
for p in range(p+1, X+1):
    y = y + P[p-1]
    if Q[q-1]<R[r-1]:
        y -= Q[q-1]
        q -= 1
    else:
        y -= R[r-1]
        r -= 1

    ans = max(ans, y)

print(ans)
    
