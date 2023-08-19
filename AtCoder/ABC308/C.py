from functools import cmp_to_key

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB = [(a, a + b, i) for i, (a, b) in enumerate(AB)]


def cmp(vl, vr):
    nl, dl, _ = vl
    nr, dr, _ = vr

    return nr * dl - nl * dr


AB.sort(key=cmp_to_key(cmp))

ans = [i + 1 for _, _, i in AB]
print(*ans)
