from collections import deque

N, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

A0 = []
A1 = []
for i, row in enumerate(A):
    A0.extend(row[i % 2 :: 2])
    A1.extend(row[1 - i % 2 :: 2])

X = N * N * d
M0 = len(A0)
M1 = len(A1)
d2 = d * 2
for offset in range(1001):
    AA0 = [(a + offset) % d2 for a in A0]
    AA1 = [(a + offset) % d2 for a in A1]

    D0 = [min(a, d2 - a) for a in AA0]
    D1 = [min(a, d2 - a) for a in AA1]

    s0 = sum(D0)
    s1 = sum(D1)

    # print(AA0, AA1)
    # print(D0, D1)
    # print(s0, s1)
    # input(offset)

    if 2 * (s0 - s1 + d * M1) <= X:
        # print("case1", offset, D0, D1, (s0, s1), (s0, -s1 + d * M1))
        B0 = []
        for a in A0:
            a += offset
            a0 = a - a % d2
            a1 = a0 + d2
            # print(a, a0, a1)
            if a - a0 < a1 - a:
                B0.append(a0 - offset)
            else:
                B0.append(a1 - offset)

        B1 = []
        for a in A1:
            a += offset + d
            a0 = a - a % d2
            a1 = a0 + d2
            if a - a0 < a1 - a:
                B1.append(a0 - offset - d)
            else:
                B1.append(a1 - offset - d)

        break

    if 2 * (s1 - s0 + d * M0) <= X:
        # print("case2", offset)
        B0 = []
        for a in A0:
            a += offset + d
            a0 = a - a % d2
            a1 = a0 + d2
            if a - a0 < a1 - a:
                B0.append(a0 - offset - d)
            else:
                B0.append(a1 - offset - d)

        B1 = []
        for a in A1:
            a += offset
            a0 = a - a % d2
            a1 = a0 + d2
            if a - a0 < a1 - a:
                B1.append(a0 - offset)
            else:
                B1.append(a1 - offset)

        break


# print(B0)
# print(B1)

# C0 = [abs(a - b) for a, b in zip(A0, B0)]
# C1 = [abs(a - b) for a, b in zip(A1, B1)]
# print(C0)
# print(C1)
# print(sum(C0) + sum(C1), d * N * N / 2)

B0 = deque(B0)
B1 = deque(B1)
ans = []
for i in range(N):
    row = []
    for j in range(N):
        p = (i + j) % 2
        if p % 2:
            row.append(B1.popleft())
        else:
            row.append(B0.popleft())
    ans.append(row)

for row in ans:
    print(*row)
