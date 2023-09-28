from itertools import permutations

C = [tuple(map(int, input().split())) for _ in range(3)]
C = C[0] + C[1] + C[2]

# 3 4 5 7
# 0 1 2 0
# 3 4 5 1
# 6 7 8 2
#       6

R = [
    [0, 3, 6],
    [0, 4],
    [0, 5, 7],
    [1, 3],
    [1, 4, 6, 7],
    [1, 5],
    [2, 3, 7],
    [2, 4],
    [2, 5, 6],
]

ans = 0
total = 0
for order in permutations(range(9)):
    X = [None] * 8
    ok = True
    for i in order:
        c = C[i]
        for r in R[i]:
            if X[r] is None:
                X[r] = c
            elif X[r] == c:
                ok = False
                break
            else:
                X[r] = None

        if not ok:
            break

    if ok:
        ans += 1
    total += 1

print(ans / total)
