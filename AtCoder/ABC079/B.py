N = int(input())
L = [2,1]
for i in range(N-1):
    L.append(L[-2]+L[-1])
print(L[-1])
