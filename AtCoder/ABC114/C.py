def f(N, D, b=False):
    if len(N)==0: return 0 if b else 1
    
    n0 = int(N[0])
    m = 0
    for d in D:
        if d==n0:
            m += f(N[1:], D)
        if d<n0:
            m += len(D)**len(N[1:])
    return m + f('9'*len(N[1:]), D, True) if b else m

N = input()
print(( f(N,[3,5,7],True)
       -f(N,[3,5  ],True)
       -f(N,[  5,7],True)
       -f(N,[3,  7],True)
       +f(N,[3    ],True)
       +f(N,[  5  ],True)
       +f(N,[    7],True)))
