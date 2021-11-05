T = int(input())
for _ in range(T):
  N2, N3, N4 = map(int, input().split())

  N334 = min(N3 // 2, N4)
  N3 -= N334 * 2
  N4 -= N334

  N2233 = min(N2 // 2, N3 // 2)
  N2 -= N2233 * 2
  N3 -= N2233 * 2

  N244 = min(N2, N4 // 2)
  N2 -= N244
  N4 -= N244 * 2

  N2224 = min(N2 // 3, N4)
  N2 -= N2224 * 3
  N4 -= N2224

  N22222 = N2 // 5

  print(N334 + N2233 + N244 + N2224 + N22222)
