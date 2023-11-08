from collections import deque, defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]

Q = deque()
D = defaultdict(int)
for i, a in enumerate(A, 1):
    if D[a]:
        while True:
            c, l, r = Q.pop()
            if c == a:
                Q.append((a, l, i))
                break
            D[c] -= 1

    else:
        Q.append((a, i, i))
        D[a] += 1


ans = [0] * (N + 1)
for a, l, r in Q:
    for i in range(l, r + 1):
        ans[i] = a

for a in ans[1:]:
    print(a)
