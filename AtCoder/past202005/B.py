N, M, Q = map(int, input().split())
point = [N]*M
qSolved = [set() for _ in range(N)]

for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0]==1:
        _, n = query
        print(sum([point[q-1] for q in qSolved[n-1]]))            

    else:
        _, n, m = query
        point[m-1] -= 1
        qSolved[n-1].add(m)
        
