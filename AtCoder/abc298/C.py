M = 200010

N = int(input())
Q = int(input())

boxes = [[] for _ in range(N + 1)]
numbers = [set() for _ in range(M)]

ans = []

for _ in range(Q):
    query = tuple(map(int, input().split()))
    t = query[0]

    if t == 1:
        _, i, j = query
        boxes[j].append(i)
        numbers[i].add(j)

    if t == 2:
        _, i = query
        ans.append(sorted(boxes[i]))

    if t == 3:
        _, i = query
        ans.append(sorted(list(numbers[i])))

for a in ans:
    print(*a)
