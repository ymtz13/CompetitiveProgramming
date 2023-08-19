from collections import deque

H, W = map(int, input().split())

A = deque([deque(list(input())) for _ in range(H)])
B = [input() for _ in range(H)]


def test(A, B):
    for h in range(H):
        for w in range(W):
            if A[h][w] != B[h][w]:
                return False

    return True


def solve(A, B):
    for w in range(W):
        for row in A:
            row.append(row.popleft())

        for h in range(H):
            A.append(A.popleft())

            if test(A, B):
                return True

    return False


print("Yes" if solve(A, B) else "No")
