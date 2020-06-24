N = int(input())
B = [10**10] + list(map(int, input().split())) + [10**10]
A = []
for i in range(N):
    A.append(min(B[i],B[i+1]))

print(sum(A))
