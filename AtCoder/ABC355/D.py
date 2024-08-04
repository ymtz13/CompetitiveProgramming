def solve(P):
    V = []
    for l, r in P:
        V.append(l * 2)
        V.append(r * 2 + 1)
    V.sort()

    cnt = ans = 0
    for v in V:
        if v % 2 == 0:
            ans += cnt
            cnt += 1
        else:
            cnt -= 1

    return ans


N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

ans = solve(P)
print(ans)
