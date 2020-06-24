import numpy as np
M = np.array([list(map(int, input().split())) for _ in range(3)])
print('Yes' if (np.all(M[0,:]-M[0,0]==M[1,:]-M[1,0]) and
                np.all(M[0,:]-M[0,0]==M[2,:]-M[2,0]) and
                np.all(M[:,0]-M[0,0]==M[:,1]-M[0,1]) and
                np.all(M[:,0]-M[0,0]==M[:,2]-M[0,2])) else 'No')
