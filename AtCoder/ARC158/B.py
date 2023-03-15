N = int(input())
X = list(map(int, input().split()))

P = sorted([x for x in X if x > 0])
N = sorted([x for x in X if x < 0])

Y = []
for A in [P, N]:
    if len(A) > 6:
        Y.extend(A[:3])
        Y.extend(A[-3:])
    else:
        Y.extend(A)


A = []

for ix, x in enumerate(Y):
    for iy, y in enumerate(Y[ix + 1 :], ix + 1):
        for z in Y[iy + 1 :]:
            A.append((x + y + z) / (x * y * z))

print(min(A))
print(max(A))
