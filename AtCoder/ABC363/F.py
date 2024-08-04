def solve(N):
    P = [(N, [])]

    for x in range(2, 1000000):
        s = str(x)
        if "0" in s:
            continue
        r = s[::-1]
        y = int(r)
        if x > y:
            continue

        p = x * y
        if N % p != 0:
            continue

        Pnxt = P[:]

        for r, arr in P:
            arr = arr[:]
            while r % p == 0:
                r //= p
                arr.append((p, x, y))
                Pnxt.append((r, arr[:]))

        P = Pnxt

    for r, arr in P:
        s = str(r)
        if "0" in s or s != s[::-1]:
            continue

        al = [str(l) for _, l, _ in arr]
        ar = [str(r) for _, _, r in arr]
        al.append(s)

        ans = al
        ans.extend(ar[::-1])
        return "*".join(ans)

    return -1


N = int(input())
print(solve(N))
exit()

# solve(92485144676140444800000)
# exit()

from random import randint, seed

seed(100)


def gen(m):
    while True:
        v = randint(1, 9999)
        if "0" not in str(v):
            return v


def prod(arr):
    r = 1
    for a in arr:
        r *= a
    return r


for case in range(100):
    n = randint(1, 5)
    x = 1
    arr = []
    for i in range(n):
        v = gen(99999)
        w = int(str(v)[::-1])
        x *= v
        arr.append(v)
        x *= w
        arr.append(w)
        # if i > 0 or randint(1, 2) == 1:
        #     x *= w
        #     arr.append(w)
    s = solve(x)
    ss = list(map(int, s.split("*")))
    pp = prod(ss)
    print(s, ss, x, arr, pp)
    assert pp == x
    print(x, solve(x))
    print(x, arr, solve(x))
