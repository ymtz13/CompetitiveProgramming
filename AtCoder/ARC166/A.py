T = int(input())
ans = []
cases = [input().split() for _ in range(T)]


def solve(X, Y):
    Sx = [[]]
    sx = Sx[0]
    Sy = [[]]
    sy = Sy[0]
    for x, y in zip(X, Y):
        if y == "C":
            if x != "C":
                return False

            if sx:
                sx = []
                Sx.append(sx)
                sy = []
                Sy.append(sy)

        else:
            sx.append(x)
            sy.append(y)

    # print(Sx)
    # print(Sy)

    for sx, sy in zip(Sx, Sy):
        cxA = sx.count("A")
        cxC = sx.count("C")
        cyA = sy.count("A")

        dA = cyA - cxA

        if dA < 0 or cxC < dA:
            return False

        for i, x in enumerate(sx):
            if x == "C":
                if dA > 0:
                    sx[i] = "A"
                    dA -= 1
                else:
                    sx[i] = "B"

        # print(sx)
        # print(sy)
        # print()

        dB = 0
        for x, y in zip(sx, sy):
            if x == "A" and y == "B":
                dB += 1
            if x == "B" and y == "A":
                dB -= 1
            if dB < 0:
                return False

    return True


for N, X, Y in cases:
    X = list(X)
    Y = list(Y)
    ans.append(solve(X, Y))


for a in ans:
    print("Yes" if a else "No")
