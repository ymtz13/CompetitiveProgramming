from collections import deque

INF = 1 << 60

N = int(input())
X = [-INF] + list(map(int, input().split())) + [INF]
Y = [0] + list(map(int, input().split())) + [0]

prevX = X[0]
prevY = Y[0]

queue = deque()

ans = INF

for x, y in zip(X[1:], Y[1:]):
    if y > prevY:
        dy = y - prevY
        queue.append((prevX + 1, dy))

    if y < prevY:
        dy = prevY - y

        while dy:
            sx, sy = queue.popleft()
            ans = min(ans, x - 1 - sx)

            if dy < sy:
                queue.appendleft((sx, sy - dy))
                dy = 0
            else:
                dy -= sy

    prevX = x
    prevY = y

print(ans if ans < INF // 4 else -1)
