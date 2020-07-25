import numpy as np

D = int(input())
C = list(map(int, input().split()))
for d in range(D):
    S = np.array(list(map(int, input().split())))
    print(S)
    print(np.argmax(S)+1)
