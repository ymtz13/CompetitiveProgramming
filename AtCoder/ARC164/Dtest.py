from collections import deque
from itertools import combinations


def solve(S):
    stack = deque([])
    lv = 0
    ans = 0
    c1 = 0
    c2 = 0
    for i, c in enumerate(S):
        v = 1 if c == "+" else -1

        if lv and lv * v < 0:
            j = stack.pop()
            # print("match", i, j)
            c1 += 1
            c2 += i - j - 1
            ans += i - j

        else:
            stack.append(i)

        lv += v

    return ans, c1, c2


N = int(input())
ans = 0
s1 = s2 = 0
for c in combinations(range(N * 2), N):
    S = ["+"] * (N * 2)
    for i in c:
        S[i] = "-"
    s = "".join(S)
    x, c1, c2 = solve(s)
    s1 += c1
    s2 += c2
    ans += x

print(ans, s1, s2)

# base=3*20
# +++--- 2 + 4
# ++-+-- 4
# ++--+- 2
# ++---+ 2
# +-++-- 2
# +-+-+- 0
# +-+--+ 0
# +--++- 0
# +--+-+ 0
# +---++ 2
# -+++-- 2
# -++-+- 0
# -++--+ 0
# -+-++- 0
# -+-+-+ 0
# -+--++ 2
# --+++- 2
# --++-+ 2
# --+-++ 4
# ---+++ 2 + 4

#  -3  -2  -1   0  +1  +2  +3
# [ 0,  0,  0,  1,  0,  0,  0, ]
# [ 0,  0,  1,  0,  1,  0,  0, ]
# [ 0,  1,  0,  2,  0,  1,  0, ] # 1*1       = 1
# [ 1,  0,  3,  0,  3,  0,  1, ] # 1*1 + 2*1 = 3
# [ 0,  4,  0,  6,  0,  4,  0, ] # 1*3 + 2*1 = 5
# [ 0,  0, 10,  0, 10,  0,  0, ] # 1*4       = 4
# [ 0,  0,  0, 20,  0,  0,  0, ]
