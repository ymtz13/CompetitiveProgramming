N = int(input())
A = list(map(int, input().split()))
A2 = [a*a for a in A]
S = sum(A)
S2 = sum(A2)
print(N*S2 - S*S)
