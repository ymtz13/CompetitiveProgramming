def solve(N, A, B):
    if A > N:
        return False
    if B == 0:
        return True

    C = N - A
    if C == 0:
        return False

    R = (B + C - 1) // C

    R1 = min(R, A + 1)
    R2 = R - R1

    return A + R1 + 2 * R2 <= N


T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    ans = solve(N, A, B)
    print("Yes" if ans else "No")
