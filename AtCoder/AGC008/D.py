from collections import deque

N = int(input())
X = list(enumerate(map(int, input().split()), 1))

X.sort(key=lambda x: x[1])

A = [None] * (N * N + 1)
queue = deque([])

for i, x in X:
    A[x] = i
    queue.extend([i] * (i - 1))

C = [0] * (N + 1)

for j, a in enumerate(A[1:], 1):
    if a is None:
        if not queue:
            print("No")
            exit()
        v = queue.popleft()
        A[j] = v
        C[v] += 1
    else:
        if C[a] != a - 1:
            print("No")
            exit()
        queue.extend([a] * (N - a))

print("Yes")
print(*A[1:])
