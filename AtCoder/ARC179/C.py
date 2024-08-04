memo = {}


def write(i, j):
    print(f"+ {i} {j}")
    return int(input())


def compare(i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    print(f"? {i} {j}")

    v = input() == "1"
    memo[(i, j)] = v
    return v


N = int(input())

A = []
for v in range(1, N + 1):
    if len(A) == 0:
        A.append(v)
        continue

    ok = len(A)
    ng = -1
    while ok - ng > 1:
        tgt = (ok + ng) // 2
        if compare(v, A[tgt]):
            ok = tgt
        else:
            ng = tgt
    A.insert(ok, v)


for _ in range(N - 1):
    vl = A.pop(0)
    vr = A.pop(-1)

    v = write(vl, vr)
    if len(A) == 0:
        break

    ok = len(A)
    ng = -1
    while ok - ng > 1:
        tgt = (ok + ng) // 2
        if compare(v, A[tgt]):
            ok = tgt
        else:
            ng = tgt
    A.insert(ok, v)

print("!")
