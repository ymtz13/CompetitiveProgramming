N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

CA = [0] * (N + 1)
CB = [0] * (N + 1)
for v in A:
    CA[v] += 1
for v in B:
    CB[v] += 1

if CA != CB:
    print("No")
    exit()

if CA[1:].count(1) < N:
    print("Yes")
    exit()

Z = sorted([(a, b) for a, b in zip(A, B)])
D = [0] + [b for _, b in Z]

cnt = 0
visited = [False] * (N + 1)
for st in range(1, N + 1):
    if visited[st]:
        continue

    H = []
    i = st
    while not visited[i]:
        visited[i] = True
        H.append(i)
        i = D[i]

    f = False
    loop = []
    for h in H:
        if h == i:
            f = True
        if f:
            loop.append(h)

    if len(loop) > 1:
        cnt += len(loop) - 1

print("Yes" if cnt % 2 == 0 else "No")
