import numpy as np

A, B, C = list(map(int, input().split()))

def f(t):
    return A*t + B*np.sin(np.pi*C*t)

for t in np.arange(0, 200, 0.001):
    if f(t)>100: break

tp = t
tn = t-0.001
for i in range(10000):
    t = (tp+tn)/2
    if f(t)>100:
        tp = t
    else:
        tn = t
print(t)
        

# f(t)  = At + Bsin(Dt)      (D:=pi*C)
# f'(t) = A + BDcos(Dt)

# A + BDcos(Dt) = 0
# cos(Dt) = -A/BD
# Dt = acos(-A/BD) + 


# make guess

