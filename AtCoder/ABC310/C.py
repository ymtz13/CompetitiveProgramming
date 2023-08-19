def f(S):
    rS = S[::-1]
    return S if S < rS else rS


N = int(input())
S = {f(input()) for _ in range(N)}


print(len(S))
