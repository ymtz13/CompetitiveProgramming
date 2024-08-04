def query(i):
    print(i)
    s = input()
    if s == "Vacant":
        exit()
    return 0 if s == "Male" else 1


N = int(input())

l = 0
r = N
vl = query(0)

while r - l > 1:
    t = (l + r) // 2
    vt = query(t)

    if (t - l) & 1 != vl ^ vt:
        r = t
    else:
        l = t
        vl = vt
