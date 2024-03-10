def solve(A, B):
    for i in range(6):
        c = min(A[i], B[i])
        A[i] -= c
        B[i] -= c

    if A[5]:
        return False

    c = min(A[4], B[5])
    A[4] -= c
    B[5] -= c
    B[1] += c
    if A[4]:
        return False

    c = min(A[3], B[5])
    A[3] -= c
    B[5] -= c
    B[2] += c
    c = min(A[3], B[4])
    A[3] -= c
    B[4] -= c
    B[1] += c
    if A[3]:
        return False

    c = min(A[2], B[5])
    A[2] -= c
    B[5] -= c
    B[3] += c
    c = min(A[2], B[4])
    A[2] -= c
    B[4] -= c
    B[2] += c
    c = min(A[2], B[3])
    A[2] -= c
    B[3] -= c
    B[1] += c
    c = min(A[2], B[2])
    A[2] -= c
    B[2] -= c
    if A[2]:
        return False

    for i in range(2, 6):
        B[1] += B[i] * i
        B[i] = 0

    return A[1] <= B[1]


T = int(input())
ans = []
for _ in range(T):
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    ans.append("Yes" if solve(A, B) else "No")

for a in ans:
    print(a)
