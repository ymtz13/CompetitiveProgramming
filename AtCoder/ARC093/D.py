A, B = list(map(int,input().split()))
N, M = max(A,B), min(A,B)
H = 10

col = (N-1)//H+1
grid = [[0 if (r%2==1)^(c//3%2==0) else 1 for c in range(col*3) ] for r in range(H*2)]
from pprint import pprint
#pprint(grid)

for i in range(1, H*col-M+1):
    pass

pprint(grid)
