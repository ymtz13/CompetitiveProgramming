N = int(input())
A = list(map(int, input().split()))
D = {}
for a in A:
    if a not in D: D[a] = 0
    D[a] += 1

n2 = 0
for k in D:
    D[k] = 2 if D[k]%2==0 else 1
    if D[k]==2: n2+=1

print(len(D) - n2%2)
