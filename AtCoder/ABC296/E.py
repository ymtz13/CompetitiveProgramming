N = int(input())
A = [0] + list(map(int, input().split()))

visited = [False] * (N + 1)
loop = [False] * (N + 1)
for st in range(1, N + 1):
    if visited[st]:
        continue

    H = []
    i = st
    while not visited[i]:
        visited[i] = True
        H.append(i)
        i = A[i]

    f = False
    for h in H:
        if h == i:
            f = True
        if f:
            loop[h] = True


print(loop.count(True))
