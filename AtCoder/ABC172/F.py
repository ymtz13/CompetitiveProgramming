N = int(input())
A = list(map(int, input().split()))
B = 0
for a in A[2:]: B^=a

print(B)
print('{:b}'.format(B))
