def moveL(P):
    if "#" in [row[0] for row in P]:
        return None

    return [row[1:] + "." for row in P]


def moveR(P):
    if "#" in [row[-1] for row in P]:
        return None

    return ["." + row[:-1] for row in P]


def moveU(P):
    if "#" in P[0]:
        return None

    return P[1:] + ["...."]


def moveD(P):
    if "#" in P[-1]:
        return None

    return ["...."] + P[:-1]


def rotR(P):
    return ["".join(c) for c in zip(*P[::-1])]


def pprint(P):
    if not P:
        print(P)
        return
    for row in P:
        print(row)


def listup(P):
    ret = []

    for i in range(4):
        P = rotR(P)

        tmp = P
        while tmp:
            P = tmp
            tmp = moveL(tmp)

        tmp = P
        while tmp:
            P = tmp
            tmp = moveU(tmp)

        tmp = P
        while tmp:
            x = tmp
            while x:
                ret.append(x)
                x = moveD(x)
            tmp = moveR(tmp)

    return ret


def merge(P1, P2, P3):
    for r1, r2, r3 in zip(P1, P2, P3):
        for c in zip(r1, r2, r3):
            if c.count("#") != 1:
                return False

    return True


P1 = [input() for _ in range(4)]
P2 = [input() for _ in range(4)]
P3 = [input() for _ in range(4)]

L1 = listup(P1)
L2 = listup(P2)
L3 = listup(P3)

for p1 in L1:
    for p2 in L2:
        for p3 in L3:
            if merge(p1, p2, p3):
                print("Yes")
                exit()

print("No")
