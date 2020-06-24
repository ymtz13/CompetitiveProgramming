from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
X = sorted(list(permutations(list(range(1,N+1)))))
for i,x in enumerate(X):
    if x==P: a=i
    if x==Q: b=i
print(abs(a-b))
