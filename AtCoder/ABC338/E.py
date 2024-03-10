from collections import deque

N = int(input())
C = [None] * (2 * N)

for i in range(N):
    A, B = map(int, input().split())
    C[A - 1] = i
    C[B - 1] = i

stack = deque()

for c in C:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)


print("Yes" if stack else "No")
