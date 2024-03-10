N = int(input())
A = list(map(int, input().split()))
N = int(input())
B = list(map(int, input().split()))
N = int(input())
C = list(map(int, input().split()))
N = int(input())
X = list(map(int, input().split()))

S = set()
for a in A:
    for b in B:
        for c in C:
            S.add(a + b + c)

for x in X:
    print("Yes" if x in S else "No")
