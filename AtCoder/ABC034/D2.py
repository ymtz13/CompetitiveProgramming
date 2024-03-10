N, K = map(int, input().split())
W = []
S = []
for _ in range(N):
    w, p = map(int, input().split())
    W.append(w)
    S.append(w*p/100)



# w0 s0
# s1/w1 > s2/w2

# (s0+s1)/(w0+w1) < (s0+s2)/(w0+w2)
# (s0+s1)*(w0+w2) < (s0+s2)*(w0+w1)
# s0w2 + s1w0 + s1w2 < s0w1 + s2w0 + s2w1



# d0 = s0/w0
# d1 = s1/w1
# d+ = (s0+s1)/(w0+w1)

#     +-- [X] --+
# V --+         +-- 0
#     +-- [Y] --+

# I[X]X = V
# I[Y]Y = V
# (I[X]+I[Y])? = V

# ? = V/(I[X]+I[Y]) = V/(V/X+V/Y) = 1/(1/X+1/Y)
# 1/? = 1/X + 1/Y
