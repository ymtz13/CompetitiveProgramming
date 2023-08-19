X, Y, Z = map(int, input().split())
S = input()

dpOff = 0
dpOn = Z

for c in S:
    if c == "a":
        # X
        # Y
        # ZX
        # ZY
        # XZ
        # YZ
        # ZXZ
        # ZYZ

        dpOff_next = min(dpOff + X, dpOff + Z + Y + Z, dpOn + Z + X, dpOn + Y + Z)
        dpOn_next = min(dpOff + X + Z, dpOff + Z + Y, dpOn + Y, dpOn + Z + X + Z)
    else:
        dpOff_next = min(dpOff + Y, dpOff + Z + X + Z, dpOn + Z + Y, dpOn + X + Z)
        dpOn_next = min(dpOff + Y + Z, dpOff + Z + X, dpOn + X, dpOn + Z + Y + Z)

    dpOff = dpOff_next
    dpOn = dpOn_next


print(min(dpOff, dpOn))
