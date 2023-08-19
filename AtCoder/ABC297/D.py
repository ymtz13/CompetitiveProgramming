A, B = map(int, input().split())

ans = 0
while A != B:
    if A < B:
        A, B = B, A

    Q = A // B
    R = A % B

    if R == 0:
        ans += Q - 1
        break

    ans += Q
    A = R

print(ans)
