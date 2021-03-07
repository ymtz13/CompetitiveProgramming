N = int(input())

# 4/N  = 1/h + 1/n + 1/w
# 4hnw = N(nw + wh + hn) = Nhn + N(n+h)w
# [4hn - N(n+h)]w = Nhn

for h in range(1, 3501):
    for n in range(h, 3501):
        cL = 4*h*n - N*(n+h)
        cR = N*h*n
        if cL>0 and cR%cL==0:
            print(h, n, cR//cL)
            exit()
        