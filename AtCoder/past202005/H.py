N, L = map(int, input().split())
X = [0]*(L+4)
for x in map(int, input().split()):
    X[x+3] = 1

T1, T2, T3 = map(int, input().split())

INF = 1000000000
dp = [INF, INF, INF, 0]

for l in range(1, L+1):
    t1 = dp[-1] + T1        + X[l-1+3]*T3
    t2 = dp[-2] + T1 + T2   + X[l-2+3]*T3
    t3 = dp[-4] + T1 + T2*3 + X[l-4+3]*T3
    dp.append(min(t1,t2,t3))

g1 = dp[-1]
g2 = dp[-2] + T1//2 + T2//2   + X[L-1+3]*T3
g3 = dp[-3] + T1//2 + T2//2*3 + X[L-2+3]*T3
g4 = dp[-4] + T1//2 + T2//2*5 + X[L-3+3]*T3

print(min(g1,g2,g3,g4))
