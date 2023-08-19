N = int(input())
S = input()

M = (N + 1) // 2

nT = nA = 0

for c in S:
    if c == "T":
        nT += 1
    if c == "A":
        nA += 1

    if nT >= M or nA >= M:
        print(c)
        exit()
