from collections import deque

N = int(input())
S = input()

D = [None] * (N + 1)
queue = deque()

for i, c in enumerate(S):
    if c == "(":
        queue.append(i)
    if c == ")" and queue:
        j = queue.pop()
        D[j] = i

ans = []
i = 0
while i < N:
    if D[i] is not None:
        i = D[i] + 1
        continue
    ans.append(S[i])
    i += 1

print("".join(ans))
