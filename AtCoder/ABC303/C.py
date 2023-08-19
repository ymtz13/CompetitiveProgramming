N, M, H, K = map(int, input().split())
S = input()
I = set()
for _ in range(M):
    x, y = map(int, input().split())
    I.add((x, y))

x = y = 0
hp = H
for c in S:
    if c == "R":
        x += 1
    if c == "L":
        x -= 1
    if c == "U":
        y += 1
    if c == "D":
        y -= 1
    hp -= 1

    if hp < 0:
        print("No")
        exit()

    if hp < K and (x, y) in I:
        I.remove((x, y))
        hp = K


print("Yes")
