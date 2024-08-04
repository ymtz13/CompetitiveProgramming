A = 0
B = 1


def solve(S):
    S = [A if c == "A" else B for c in S]

    cnt = 0
    n = 0
    queue = [None] * len(S)

    for c in S:
        queue[n] = c
        n += 1

        # print(queue[:n])

        while n >= 3 and queue[n - 3 : n] == [A, A, B]:
            n -= 3
            cnt += 1

    Sf = queue[:n][::-1]
    queue = [None] * len(Sf)
    n = 0
    for c in Sf:
        queue[n] = c
        n += 1

        while n >= 3 and queue[n - 3 : n] == [A, A, B]:
            n -= 3
            cnt += 1

    return cnt


X = [
    "AABAAAB",
    "BAAAAABBA",
    "A",
    "B",
    "ABA",
    "BAA",
    "AAAAAA",
    "AAAABB",
    "AABABBAABBABAAAABBAA",
    "BBAAAAABAAAAABABAABA",
]

# print(X[8], solve(X[8]))


T = int(input())
ans = []
for _ in range(T):
    S = input()
    ans.append(solve(S))

for a in ans:
    print(a)
