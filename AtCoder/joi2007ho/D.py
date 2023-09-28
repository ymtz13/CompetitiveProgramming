N = int(input())
M = int(input())
E = [[] for _ in range(N)]
D = [0] * N
for _ in range(M):
    i, j = map(int, input().split())
    E[i - 1].append(j - 1)
    D[j - 1] += 1

queue = [i for i, d in enumerate(D) if d == 0]

ans = []
multi = False
while queue:
    if len(queue) > 1:
        multi = True

    ans.extend(queue)

    queue_next = []
    for q in queue:
        for e in E[q]:
            D[e] -= 1
            if D[e] == 0:
                queue_next.append(e)

    queue = queue_next

for a in ans:
    print(a + 1)
print(1 if multi else 0)
