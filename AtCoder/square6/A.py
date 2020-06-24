N, T = [int(c) for c in input().split()]
A = [int(c) for c in input().split()]
SA = sum(A)
print(SA//T + int(SA%T!=0))
