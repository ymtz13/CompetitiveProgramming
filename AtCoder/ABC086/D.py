import numpy as np

from time import time

N, K = map(int, input().split())
K2 = K*2
#M = [[0]*K2 for _ in range(K2)]
#M = np.array(M)
t0 = time()


M = np.zeros((K2, K2), int)
nb = 0
for _ in range(N):
  x, y, c = input().split()
  x = int(x) % K2
  y = int(y) % K2
  if c=='B': nb+=1
  M[x, y] += 1 if c=='W' else -1

t1 = time()
print('t1:', t1-t0)

#Sx = [[0]*(K2+1) for _ in range(K2)]
Sx = np.zeros((K2, K2+1), int)
#-> for x, (s, m) in enumerate(zip(Sx, M)):
#->   #for y in range(K2):
#->   #  s[y+1] = s[y] + m[y]
#->   for y, my in enumerate(m):
#->     s[y+1] = s[y] + my

for y in range(K2):
  Sx[:, y+1] = Sx[:, y] + M[:, y]

t2 = time()
print('t2:', t2-t1)
print(Sx)    
#exit()
    
#S = [[0]*(K2+1) for _ in range(K2+1)]
S = np.zeros((K2+1, K2+1), int)
#for x in range(K2):
#  for y in range(1,K2+1):
#    S[x+1][y] = S[x][y] + Sx[x][y]

for x in range(K2):
  S[x+1] = S[x] + Sx[x]

t3 = time()
print('t3:', t3-t2)
print(S)
    
# def sc(x1, y1):
#   x0 = max(x1-K, 0)
#   y0 = max(y1-K, 0)
#   x1 = max(min(x1, K2), 0)
#   y1 = max(min(y1, K2), 0)
#   return S[x1,y1] - S[x0,y1] - S[x1,y0] + S[x0,y0]

# Y = np.empty((5, K2), int)
Y = np.arange(K2)[:, None] + np.arange(-K, K+1, K)
Y[:K, 0] = 0
Y[K:, 2] = K2
# Y[0] = np.max(0 , Y[0]-K2)
# Y[1] = np.max(0 , Y[1]-K )
# Y[3] = np.min(K2, Y[3]+K )
# Y[4] = K2
print(Y)

ans = -10000000
for x in range(K2):
  x0 = 0 #max(x-K2, 0)
  x1 = max(x-K , 0)
  x2 = x
  x3 = min(x+K , K2)
  x4 = K2

  T1 = S[x4] - S[x3] + S[x2] - S[x1]
  T2 = S[x3] - S[x2] + S[x1] - S[x0]

  U = T1[K2] - T1[K:K2] + T1[:K] + T2[K:K2] - T2[:K]
  
  #for y in range(K):
  #  score = T1[K2] - T1[y+K] + T1[y] + T2[y+K] - T2[y]
  #  ans = max(ans, score)
  #
  #for y in range(K, K2):
  #  score = T1[K2] - T1[y] + T1[y-K] + T2[y] - T2[y-K]
  #  ans = max(ans, score)      

#print(nb+ans)
print(nb + np.max(U))

t4 = time()
print('t4:', t4-t3)
