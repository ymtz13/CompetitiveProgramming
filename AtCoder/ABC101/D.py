K = int(input())
candidates = list(range(1, 100000))

for d in range(6, 25):
    r = 10 ** (d - 5)
    for x in range(10**4, 10**5):
        candidates.append(x * r + r - 1)

C = []
cmin = (10**21, 1)
for n in reversed(candidates):
    denom = sum(map(int, str(n)))

    if n * cmin[1] <= cmin[0] * denom:
        C.append(n)
        cmin = (n, denom)


C.reverse()

for c in C[:K]:
    print(c)
