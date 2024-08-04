from itertools import permutations


def solve(N, H, W, R):
    cnt = 0
    for perm in permutations(range(N)):
        cnt += 1
    print(cnt)


solve(7, 1, 1, [])


N, H, W = map(int, input().split())
R = [tuple(map(int, input().split())) for _ in range(N)]
