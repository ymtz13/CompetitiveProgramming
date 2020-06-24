N, M = list(map(int, input().split()))

f1, f2 = [], []

k = 1
while k*k<=M:
    if M%k==0:
        f1.append(k)
        f2.append(M//k)
    k+=1

for f in f1 + list(reversed(f2)):
    if f>=N:
        print(M//f)
        break
