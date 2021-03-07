# f = x + P * 2^(-2x/3) = x + Pexp(-(2log2)x/3) = x + Pexp(-x/T)
# df/dx = 1 - (P/T)exp(-x/T)

# exp(-x/T) = T/P
# -x/T = log(T/P)
# x = -Tlog(T/P)

# f(x) = -Tlog(T/P) + T

from math import log
T = 1.5/log(2)
P = float(input())
x = -T*log(T/P)
print(x+T if x>0 else P)