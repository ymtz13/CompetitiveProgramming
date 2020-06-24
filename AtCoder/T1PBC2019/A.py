x = [int(c) for c in input().split()]
if (x[0]<x[2] and x[2]<x[1]) or (x[1]<x[2] and x[2]<x[0]):
    print('Yes')
else:
    print('No')
