from collections import deque

X, Y, N = map(int, input().split())

Z = []

for i in range(1, N + 1):
    x1, y1, x2, y2 = map(int, input().split())
    z = []

    for x, y in [(x1, y1), (x2, y2)]:
        if x == 0:
            z.append((2 * X + 2 * Y - y, i))
            continue
        if x == X:
            z.append((X + y, i))
            continue
        if y == 0:
            z.append((x, i))
            continue
        if y == Y:
            z.append((2 * X + Y - x, i))

    if len(z) == 2:
        Z.extend(z)

Z.sort()

stack = deque()
for _, i in Z:
    if stack and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)


print("NO" if stack else "YES")
