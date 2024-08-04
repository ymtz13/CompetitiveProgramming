from collections import deque
from itertools import permutations

N, H, W = map(int, input().split())
R = [tuple(map(int, input().split())) for _ in range(N)]

H1 = H + 1
W1 = W + 1
HW = H1 * W1
board = [-1] * HW

for h in range(H1):
    board[h * W1] = 9
for w in range(W1):
    board[w] = 9


def pboard():
    for h in range(0, H1):
        bb = board[h * W1 : h * W1 + W1]
        print(bb)


stack = deque([(i, 0, 0) for i in range(N)] + [(i, 1, 0) for i in range(N)])
used = [False] * N
used_cnt = 0
placement = deque()
s = 0
while stack:
    q, rot, t = stack.pop()
    pH, pW = R[q]
    if rot:
        pH, pW = pW, pH
    pS = pH * pW

    if t == 0:
        stack.append((q, None, 1))
        used[q] = True
        used_cnt += 1
        placement.append((q, rot))

        f = False
        for h in range(1, H1):
            for w in range(1, W1):
                i = h * W1 + w
                if board[i] == -1:
                    f = True
                    break
            if f:
                break

        s += pS

        if h + pH > H1 or w + pW > W1:
            continue

        f = False
        for hh in range(h, h + pH):
            for ww in range(w, w + pW):
                ii = hh * W1 + ww
                if board[ii] != -1:
                    f = True
                    break
                board[ii] = q
            if f:
                break

        if f:
            continue

        # print(placement, (h, w))
        # pboard()
        # input()

        if s == H * W:
            print("Yes")
            exit()

        for p, u in enumerate(used):
            if u:
                continue
            stack.append((p, 0, 0))
            stack.append((p, 1, 0))
    else:
        used[q] = False
        used_cnt -= 1
        placement.pop()
        s -= pS

        for h in range(1, H1):
            for w in range(1, W1):
                i = h * W1 + w
                if board[i] == q:
                    board[i] = -1

print("No")
