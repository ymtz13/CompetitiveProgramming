N = int(input())
for k in range(int(N**0.5), 0, -1):
    if N%k==0:
        print(k+N//k-2)
        break
