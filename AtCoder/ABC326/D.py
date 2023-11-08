from itertools import product

N = int(input())
R = input()
C = input()


def s(iA, iB, iC):
    ss = ["."] * N
    ss[iA] = "A"
    ss[iB] = "B"
    ss[iC] = "C"
    return "".join(ss)


SA = []
SB = []
SC = []

for i1 in range(N - 2):
    for i2 in range(i1 + 1, N - 1):
        for i3 in range(i2 + 1, N):
            SA.append(s(i1, i2, i3))
            SA.append(s(i1, i3, i2))
            SB.append(s(i2, i1, i3))
            SB.append(s(i3, i1, i2))
            SC.append(s(i2, i3, i1))
            SC.append(s(i3, i2, i1))


SS = {"A": SA, "B": SB, "C": SC}

for P in product(*[SS[r] for r in R]):
    # print(P)

    cols = [[p[ic] for p in P if p[ic] != "."] for ic in range(N)]

    ok = True
    for col, c in zip(cols, C):
        if sorted(col) != ["A", "B", "C"]:
            ok = False
            break

        if col[0] != c:
            ok = False
            break

    if ok:
        print("Yes")
        for p in P:
            print("".join(p))
        exit()


print("No")
