N = int(input())
S = [ord(c) for c in input()]

L = 0
R = N - 1

for c in range(ord('a'), ord('z') + 1):
  while L < N and S[L] == c:
    L += 1

  for r in range(R, 0, -1):
    if r <= L: break
    if S[r] == c:
      S[L], S[r] = S[r], S[L]

      L += 1
      while S[L] == c:
        L += 1

      R = r - 1

print(''.join(map(chr, S)))
