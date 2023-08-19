def ans(b):
    print("Yes" if b else "No")
    exit()


S = input()

iB = []
iR = []

for i, c in enumerate(S):
    if c == "B":
        iB.append(i)
    if c == "R":
        iR.append(i)
    if c == "K":
        iK = i

iB0, iB1 = iB
if (iB0 + iB1) % 2 == 0:
    ans(False)

iR0, iR1 = sorted(iR)
ans(iR0 < iK and iK < iR1)
