from collections import deque

L, N1, N2 = map(int, input().split())
A1 = deque([tuple(map(int, input().split())) for _ in range(N1)])
A2 = deque([tuple(map(int, input().split())) for _ in range(N2)])

L1 = L2 = 0
V1 = V2 = None
ans = 0

while A1 or A2:
    if L1 <= L2:
        v1, l1 = A1.popleft()

        d = L2 - L1
        if V2 == v1:
            ans += min(d, l1)

        L1 += l1
        V1 = v1

    else:
        v2, l2 = A2.popleft()

        d = L1 - L2
        if V1 == v2:
            ans += min(d, l2)

        L2 += l2
        V2 = v2

print(ans)
