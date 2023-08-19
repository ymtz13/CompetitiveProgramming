from collections import deque

mod = 998244353

Q = int(input())
A = deque([1])
M = 1

ans = []

for _ in range(Q):
    query = tuple(map(int, input().split()))
    t = query[0]

    if t == 1:
        _, x = query
        A.append(x)
        M = (M * 10 + x) % mod

    if t == 2:
        x = A.popleft()
        M = (M - x * pow(10, len(A), mod)) % mod

    if t == 3:
        ans.append(M)

for a in ans:
    print(a)
