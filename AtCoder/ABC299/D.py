N = int(input())
L = 1
R = N

while R - L > 1:
    tgt = (R + L) // 2
    print("?", tgt)
    s = int(input())
    if s == 0:
        L = tgt
    else:
        R = tgt

print("!", L)
