N = int(input())
S = list(map(int, input()))
C = list(map(int, input().split()))

XL0 = [0]
XL1 = [0]

for i, (s, c) in enumerate(zip(S, C)):
    p = i % 2
    if p == s:
        XL0.append(XL0[-1])
        XL1.append(XL1[-1] + c)
    else:
        XL0.append(XL0[-1] + c)
        XL1.append(XL1[-1])

XR0 = [0]
XR1 = [0]

for i, (s, c) in enumerate(zip(S[::-1], C[::-1])):
    p = i % 2
    if p == s:
        XR0.append(XR0[-1])
        XR1.append(XR1[-1] + c)
    else:
        XR0.append(XR0[-1] + c)
        XR1.append(XR1[-1])

ans = sum(C)
if N % 2 == 0:
    for nL in range(1, N):
        nR = N - nL
        c0 = XL0[nL] + XR0[nR]
        c1 = XL1[nL] + XR1[nR]
        ans = min(ans, c0, c1)
else:
    for nL in range(1, N):
        nR = N - nL
        c0 = XL0[nL] + XR1[nR]
        c1 = XL1[nL] + XR0[nR]
        ans = min(ans, c0, c1)

print(ans)
