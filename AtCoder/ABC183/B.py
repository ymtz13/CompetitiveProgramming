Sx, Sy, Gx, Gy = map(int, input().split())
Dx = Gx-Sx
Dy = Sy+Gy
x = Sy/Dy*Dx
ans = Sx+x
print(ans)