import numpy as np
import matplotlib.pyplot as plt

def s(n):
    r = 0
    while n:
        r+=n%10
        n//=10
    return r

N = np.arange(1,10**5)
#N=[]
#for i in range(16):
#  for j in range(1, 10):
#    N.append((j+1)*(10**i)-1)

S = []
for n in N:
    S.append(s(n))
S = np.array(S)

#plt.plot(N,S)
#plt.plot(N,S/N)
plt.plot(N,N/S)
#plt.plot(np.log(N),np.log(S/N))
plt.grid()
plt.show()
