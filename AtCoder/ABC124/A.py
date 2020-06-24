A,B = [int(c) for c in input().split()]
if A>B:
    print(A*2-1)
elif A==B:
    print(A*2)
else:
    print(B*2-1)
