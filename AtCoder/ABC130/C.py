W, H, x, y = [int(c) for c in input().split()]
n = 1 if x*2==W and y*2==H else 0
print(W*H/2, n)
