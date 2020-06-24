import random
import numpy as np

def f(a,b):
    retval=1
    for i in range(b):
        retval*=(a-i)
    return retval

while True:
    n, k, m, r = [int(_) for _ in input().split()]
    if(n==0): break
    print('n,k,m,r = ', n,k,m,r)

    if m==0:
        print(1/n)
        continue


    print(' X  Y  j  p(X)       p(Y,j|X)   p(last=j|X,Y,j)  p(X,Y,j,last=j)')
    s=0
    for X in range(1,(n-1)*k+1):
        for Y in range(1, min(k,X)+1):
            for j in range(2, n+1):
                dd = k*(f((n-1)*k,X) / f(n*k,X+1)) * ( f(k, Y) * f((n-j)*k, X-Y) * f(X,Y) / f(Y,Y) / f((n-1)*k, X) ) * (Y/X)
                s+=dd
                print('{:2d} {:2d} {:2d}  {:.3e}  {:.3e}  {:.3e}        {:.3e}'.format(
                    X,Y,j,k*(f((n-1)*k,X) / f(n*k,X+1)),
                    f(k,Y) * f((n-j)*k, X-Y) * f(X,Y) / f(Y,Y) / f((n-1)*k,X),
                    Y/X, dd))
    print(1/n+s)
        
    s=0
    for X in range(1,(n-1)*k+1):
        t=0
        for Y in range(1, min(k, X)+1):
            u=0
            for j in range(2, n+1):
                u += f((n-j)*k, X-Y)
            t+=u*f(k,Y)*Y*f(X,Y)/f(Y,Y)
        s+=t/(f(n*k,X+1)*X)
    print(1/n,s*k,1/n+s*k)
    
