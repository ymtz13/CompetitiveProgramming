N, M = map(int, input().split())
X = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    if a==1 or a==N: X[b-1]+=1
    if b==1 or b==N: X[a-1]+=1

print('POSSIBLE' if max(X)>=2 else 'IMPOSSIBLE')
