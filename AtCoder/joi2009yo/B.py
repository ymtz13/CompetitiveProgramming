P = [int(input()) for _ in range(20)]
P1 = sorted(P[:10])
P2 = sorted(P[10:])
print(sum(P1[-3:]), sum(P2[-3:]))
