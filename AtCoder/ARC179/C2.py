heap1 = [None] * 2048  # max heap
heap2 = [None] * 2048  # min heap
len1 = 0
len2 = 0
deleted = [False] * 2010
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


def push1(v):
    global len1

    len1 += 1
    p = len1
    heap1[p] = v
    while p > 1:
        q = p >> 1

        i = heap1[p]
        j = heap1[q]

        if not deleted[j]:
            i_is_smaller = compare(i, j)
            if i_is_smaller:
                break

        heap1[p] = j
        heap1[q] = i

        p = q


def push2(v):
    global len2

    len2 += 1
    p = len2
    heap2[p] = v
    while p > 1:
        q = p >> 1

        i = heap2[p]
        j = heap2[q]

        if not deleted[j]:
            i_is_smaller = compare(i, j)
            if not i_is_smaller:
                break

        heap2[p] = j
        heap2[q] = i

        p = q


def pop1():
    global len1

    while True:
        ret = heap1[1]

        while True:
            v = heap1[len1]
            heap1[len1] = None
            len1 -= 1

            if not deleted[v]:
                break

        heap1[1] = v

        p = 1
        while p < 1024:
            i = heap1[p]

            ql = p << 1
            j = heap1[ql]
            if j is None:
                break

            i_is_smaller = deleted[j] or compare(i, j)
            if i_is_smaller:
                heap1[p] = j
                heap1[ql] = i
                p = ql
                continue

            qr = ql + 1
            j = heap1[qr]
            if j is None:
                break

            i_is_smaller = deleted[j] or compare(i, j)
            if i_is_smaller:
                heap1[p] = j
                heap1[qr] = i
                p = qr
                continue

            break

        if not deleted[ret]:
            return ret


def pop2():
    global len2

    while True:
        ret = heap2[1]

        while True:
            v = heap2[len2]
            heap2[len2] = None
            len2 -= 1

            if not deleted[v]:
                break

        heap2[1] = v

        p = 1
        while p < 1024:
            i = heap2[p]

            ql = p << 1
            j = heap2[ql]
            if j is None:
                break

            i_is_greater = deleted[j] or not compare(i, j)
            if i_is_greater:
                heap2[p] = j
                heap2[ql] = i
                p = ql
                continue

            qr = ql + 1
            j = heap2[qr]
            if j is None:
                break

            i_is_greater = deleted[j] or not compare(i, j)
            if not i_is_greater:
                heap2[p] = j
                heap2[qr] = i
                p = qr
                continue

            break

        if not deleted[ret]:
            return ret


N = int(input())
for i in range(1, N + 1):
    push1(i)
    push2(i)
    # print(heap1[:10])
    # print(heap2[:10])

for _ in range(N - 1):
    imax = pop1()
    imin = pop2()

    deleted[imax] = True
    deleted[imin] = True

    j = write(imax, imin)
    if j == N * 2 - 1:
        break

    push1(j)
    push2(j)

    # print(heap1[:10])
    # print(heap2[:10])


print("!")
