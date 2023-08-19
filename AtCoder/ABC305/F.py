N, M = map(int, input().split())

current = 1
visited = [False] * (N + 1)
parent = [None] * (N + 1)

while current != N:
    visited[current] = True

    V = list(map(int, input().split()))[1:]

    nextnode = None
    for v in V:
        if not visited[v]:
            nextnode = v
            break

    if nextnode is not None:
        print(nextnode)
        parent[nextnode] = current
        current = nextnode

    else:
        current = parent[current]
        print(current)
