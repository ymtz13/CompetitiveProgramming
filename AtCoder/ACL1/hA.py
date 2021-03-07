class UF:
    def __init__(self, N):
        self.uf = [-1]*N
        self.n = N

    def find(self, x):
        if self.uf[x]<0: return x
        self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x==y: return
        if self.size(x) > self.size(y): x, y = y, x
        self.uf[y] += self.uf[x]
        self.uf[x] = y
        self.n -= 1


def solve_exact(XYI):
    N = len(XYI)
    uf = UF(N)
    
    ans = [1]*N
    for p in range(N):
        xp, yp, ip = XYI[p]
        for q in range(p+1, N):
            xq, yq, iq = XYI[q]
            if (xp>xq and yp>yq) or (xp<xq and yp<yq):
                uf.union(ip, iq)
    return [uf.size(i) for i in range(N)]

def solve(XYI):
    N = len(XYI)
    uf = UF(N)

    pi = None
    py = N+1
    for x, y, i in XYI:
        if y>py: uf.union(i, pi)
        else:
            pi = i
            py = y

    pi = None
    py = 0
    for x, y, i in reversed(XYI):
        if y<py: uf.union(i, pi)
        else:
            pi = i
            py = y

    ans = [uf.size(i) for i in range(N)]
    return ans


def solve2(XYI):
    N = len(XYI)
    uf = UF(N)

    pi = None
    py = N+1
    for x, y, i in XYI:
        if y>py: uf.union(i, pi)
        else:
            pi = i
            py = y

    XYI = [(y, x, i) for x, y, i in XYI]
    XYI.sort()

    pi = None
    py = 0
    for x, y, i in reversed(XYI):
        if y<py: uf.union(i, pi)
        else:
            pi = i
            py = y

    pi = None
    py = N+1
    for x, y, i in XYI:
        if y>py: uf.union(i, pi)
        else:
            pi = i
            py = y

    pi = None
    py = 0
    for x, y, i in reversed(XYI):
        if y<py: uf.union(i, pi)
        else:
            pi = i
            py = y


    ans = [uf.size(i) for i in range(N)]
    return ans


def test(XYI):
    from random import seed, shuffle
    seed(s)
    
    X = 8
    Y = list(range(X))
    shuffle(Y)
    XYI = [(x, y, x) for x, y in enumerate(Y)]

    ans = solve2(XYI)
    ans_exact = solve_exact(XYI)

    error = False
    for a, ae in zip(ans, ans_exact):
        if a!=ae:
            error=True
            break
        
    return error, s, Y, ans, ans_exact
    

if __name__=='__main__':
    for s in range(10000000):
        error, s, Y, ans, ans_exact = test(s)
        if error:
            print('error!!!')
            print(s, Y)
            print(ans)
            print(ans_exact)
            for y in Y:
                r = [' ']*len(Y)
                r[y] = 'x'
                print(''.join(r))
            print()
        
X = 8
A = [None]*X
