N = int(input())
A = list(map(int, input().split()))

if A[0]==1:
    print(1 if N==0 else -1)
    exit()

if A[0]>1:
    print(-1)
    exit()
    

INF = 10**15

cond = [1]
m = INF
for a in A[1:]:
    c = min(INF, cond[-1]*2-a)
    if c<0:
        print(-1)
        exit()
    cond.append(c)

ans = 0
node = 0
for n in range(N, -1, -1):
    n1 = A[n]
    n2 = min(cond[n], node)
    node = n1 + n2
    ans += node

print(ans)
