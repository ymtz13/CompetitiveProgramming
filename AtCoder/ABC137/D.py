from bisect import bisect_left

N, M = list(map(int, input().split()))
M_max = 10**5+1
B = [[] for _ in range(M_max)]
for _ in range(N):
    a,b = list(map(int, input().split()))
    B[a].append(b)

for a in range(M_max):
    B[a] = sorted(B[a])
    
queue = []
ans = []
for m in range(1,M+1):
    if B[m]:
        b = B[m].pop(-1)
        idx = bisect_left(queue, (b, m))
        queue.insert(idx, (b, m))

    if queue:
        b, a = queue.pop(-1)
        ans.append(b)
        if B[a]:
            b_ = B[a].pop(-1)
            idx = bisect_left(queue, (b_, a))
            queue.insert(idx, (b_, a))

    #print(queue)
    #print(ans)
    #print()

print(sum(ans))
