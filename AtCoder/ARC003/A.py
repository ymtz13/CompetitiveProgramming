N = int(input())
R = input()
S = sum([max(0, ord('E')-ord(r)) for r in R])
print(S/N)
