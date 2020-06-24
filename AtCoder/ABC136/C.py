N = int(input())
H = list(map(int, input().split()))
f = True
for i in range(1, N):
    if H[i]>H[i-1]:
        H[i]-=1
    if H[i]<H[i-1]:
        f = False
        break

print('Yes' if f else 'No')
