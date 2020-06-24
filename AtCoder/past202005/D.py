import numpy as np
N = int(input())
display = np.empty((5, 4*N+1), bool)
for i in range(5):
    display[i] = np.array([c=='#' for c in input()])

s = [None]*5
s[0] = ".###..#..###.###.#.#.###.###.###.###.###."
s[1] = ".#.#.##....#...#.#.#.#...#.....#.#.#.#.#."
s[2] = ".#.#..#..###.###.###.###.###...#.###.###."
s[3] = ".#.#..#..#.....#...#...#.#.#...#.#.#...#."
s[4] = ".###.###.###.###...#.###.###...#.###.###."


display_example = np.empty((5,41), bool)
for i in range(5):
    display_example[i] = np.array([c=='#' for c in s[i]])

ans = []
for n in range(N):
    c = display[:, n*4+1:n*4+4]
    for m in range(10):
        if np.all(c==display_example[:, m*4+1:m*4+4]):
            ans.append(m)
            break

print(''.join(map(str, ans)))
