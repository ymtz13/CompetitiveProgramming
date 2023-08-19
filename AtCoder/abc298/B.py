N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]


def test(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] and not B[i][j]:
                return False

    return True


def rot(A):
    R = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            R[i][j] = A[N - 1 - j][i]

    return R


for _ in range(4):
    if test(A, B):
        print("Yes")
        exit()

    A = rot(A)

print("No")
