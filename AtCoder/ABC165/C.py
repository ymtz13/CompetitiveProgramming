N, M, Q = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(Q)]

def dfs(i):
    global cnt
    
    if i==N+1:
        print(A)
        cnt+=1
        return
    
    for a in range(A[i-1], M+1):
        A[i]=a
        dfs(i+1)

cnt = 0
A = [1]*(N+1)
dfs(1)

print(cnt)
