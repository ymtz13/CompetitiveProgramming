import numpy as np
from random import random
from time import time

V = 10**10
X = 10**7
A = np.random.randint(-V, V, X)
B = list(A)

A_bgn = time()
for i in range(X):
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
  z = A[i]
A_end = time()

B_bgn = time()
for i in range(X):
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
  z = B[i]
B_end = time()

print(A_end - A_bgn)
print(B_end - B_bgn)
