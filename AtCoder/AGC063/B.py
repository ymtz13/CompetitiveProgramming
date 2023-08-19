from collections import deque

N = int(input())
A = list(map(int, input().split()))

stack = deque([])
ans = 0

for a in A:
    if a == 1:
        stack.append(1)
    else:
        while stack:
            v = stack.pop()
            if v == a - 1:
                stack.append(a)
                break

    ans += len(stack)

print(ans)
