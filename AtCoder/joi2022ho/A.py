from collections import deque

N = int(input())
A = deque([int(input()) for _ in range(N)])
Q = int(input())
X = [int(input()) for _ in range(Q)]

M = 0
for x in X:
    while M < x:
        a = A.popleft()
        k = 1
        while a % 2 == 0:
            a //= 2
            k *= 2
        M += k

    print(a)
