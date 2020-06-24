n = int(input())
p = [int(c) for c in input().split()]

c = 0
for i in range(1,n-1):
    if p[i-1] < p[i] and p[i] < p[i+1]: c+=1
    if p[i-1] > p[i] and p[i] > p[i+1]: c+=1

print(c)
