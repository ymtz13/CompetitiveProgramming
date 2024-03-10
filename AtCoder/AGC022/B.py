A = [(v - 2, v) for v in range(10, 30001, 6)]
B = [(v - 6, v) for v in range(21, 30001, 12)]
C = list(range(6, 30001, 6))
D = A + B


def solve(N: int):
    if N == 3:
        return [2, 5, 63]

    ans = [2, 3, 4, 9]
    for x, y in D[: (N - 4) // 2]:
        ans.append(x)
        ans.append(y)

    ans.extend(C[: N - len(ans)])

    return ans


N = int(input())
print(*solve(N))
