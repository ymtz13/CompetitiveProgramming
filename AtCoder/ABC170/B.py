X, Y = map(int, input().split())
for nc in range(X+1):
    nt = X-nc
    if Y==nc*2+nt*4:
        print("Yes")
        exit()
print("No")
