N, K = map(int, input().split())
A = list(map(int, input().split()))

DL = []
for p, q in zip(A[0::2], A[1::2]):
    DL.append(q - p)

if K % 2 == 0:
    print(sum(DL))
    exit()

DR = []
for p, q in zip(A[1::2], A[2::2]):
    DR.append(q - p)

ans = s = sum(DR)
for dl, dr in zip(DL, DR):
    s += dl
    s -= dr
    ans = min(ans, s)

print(ans)
