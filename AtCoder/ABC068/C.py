import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
T1 = [False]*(N+1)
TN = [False]*(N+1)

for _ in range(M):
    a, b = list(map(int, input().split()))
    if a==1: T1[b]=True
    if b==N: TN[a]=True

for t1, tn in zip(T1,TN):
    if t1 and tn:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
