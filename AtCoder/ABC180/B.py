N = int(input())
X = tuple(map(int, input().split()))
A = tuple(map(abs ,X))

print(sum(A))
print(sum([x*x for x in X])**0.5)
print(max(A))
