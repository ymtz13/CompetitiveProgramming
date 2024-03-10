from itertools import product

F = [[0] * 40 for _ in range(40)]
for p in range(-10, 20):
    for q in range(-10, 20):
        F[p][q] = max(0, min(p, q) - max(p, q) + 7)


def f3(p, q, r):
    return max(0, min(p, q, r) - max(p, q, r) + 7)


V1, V2, V3 = map(int, input().split())

x1 = y1 = z1 = 0

cnt = 0
for x2, y2, z2 in product(range(8), repeat=3):
    if x2 > y2 or y2 > z2:
        continue

    for x3, y3, z3 in product(range(-8, x2 + 9), range(-8, y2 + 9), range(-8, z2 + 9)):
        cnt += 1
        v12 = F[x1][x2] * F[y1][y2] * F[z1][z2]
        v23 = F[x2][x3] * F[y2][y3] * F[z2][z3]
        v31 = F[x3][x1] * F[y3][y1] * F[z3][z1]
        v3 = f3(x1, x2, x3) * f3(y1, y2, y3) * f3(z1, z2, z3)

        v2 = v12 + v23 + v31 - v3 * 3

        v1 = 343 * 3 - v2 * 2 - v3 * 3

        if v1 == V1 and v2 == V2 and v3 == V3:
            print("Yes")
            print(x1, y1, z1, x2, y2, z2, x3, y3, z3)
            exit()

# print(cnt)
print("No")
