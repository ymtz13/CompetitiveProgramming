from math import log, e
from random import random
import matplotlib.pyplot as plt

l = 1e-5


def sample():
    return -log(random()) / l


X = [round(sample()) for _ in range(10000)]
print(sorted(X[:30]))
exit()

X.sort()

cnt = [0] * 10000
for x in X:
    cnt[x // 1000] += 1
    # print(x)

for i, c in enumerate(cnt):
    if c:
        print(i * 1000, c)
