H, W, N = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * 30
for a in A:
    C[a] += 1

h = H
w = W
n = 0
for i, c in enumerate(C):
    r = 0
    if h % 2:
        r += (w // 2) * 2
    if w % 2:
        r += (h // 2) * 2
    if h % 2 and w % 2:
        r += 1

    c = n + c

    n = max(0, (c - r + 3) // 4)

    h //= 2
    w //= 2


print("No" if n else "Yes")
