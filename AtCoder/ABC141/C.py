N, K, Q = list(map(int, input().split()))
P = [K-Q]*N
for _ in range(Q):
    P[int(input())-1]+=1

for p in P:
    print('Yes' if p>0 else 'No')

