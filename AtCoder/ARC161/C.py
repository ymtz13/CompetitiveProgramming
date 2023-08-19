from collections import deque

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    E = [[] for _ in range(N)]
    D = [0] * N
    for _ in range(N - 1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        E[A].append(B)
        E[B].append(A)
        D[A] += 1
        D[B] += 1
    S = input()

    Parent = [None] * N
    queue = deque([(0, None)])
    Order = []
    while queue:
        q, parent = queue.popleft()
        Order.append(q)
        Parent[q] = parent

        for e in E[q]:
            if e == parent:
                continue
            queue.append((e, q))

    Cnt = [0] * N
    Color = [None] * N

    ng = False

    for q in reversed(Order):
        deg = D[q]
        parent = Parent[q]

        if deg == 1 and q > 0:
            color = S[parent]
            Color[q] = color
            if parent is not None:
                Cnt[parent] += 1 if color == "W" else -1

        else:
            s = set()
            for e in E[q]:
                if e == parent:
                    continue
                color = S[e]

                if Cnt[e] == 0:
                    s.add(color)
                if (color == "W" and Cnt[e] < 0) or (color == "B" and Cnt[e] > 0):
                    ng = True
                    break

            # print(q + 1, s, E[q])

            if len(s) == 2:
                ng = True
                break
            else:
                if len(s) == 0:
                    color = S[parent] if parent is not None else "W"
                    # print("color of {} not decided".format(q + 1))
                else:
                    color = list(s)[0]
                    # print("color of {} should be {}".format(q + 1, color))

                Color[q] = color
                if parent is not None:
                    Cnt[parent] += 1 if color == "W" else -1

    cW = cB = 0
    for e in E[0]:
        if Color[e] == "W":
            cW += 1
        else:
            cB += 1

    if (S[0] == "W" and cW < cB) or (S[0] == "B" and cB < cW):
        ng = True

    if ng:
        ans.append(-1)
    else:
        ans.append("".join(Color))

    # print(ans[-1])

for a in ans:
    print(a)
