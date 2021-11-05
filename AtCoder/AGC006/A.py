N = int(input())
s = input()
t = input()

for n in range(N, 0, -1):
  if s[-n:] == t[:n]:
    print(N * 2 - n)
    exit()

print(N * 2)
