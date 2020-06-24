N, A, B, C, D = [int(c) for c in input().split()]
S = input()

reachable = {B-1}
unreachable = set()
for i, c in enumerate(S):
    if c=='.' and (i-2 in reachable or i-1 in reachable):
        reachable.add(i)


for x in range(A, C):
    if x>=2 and S[x-1]=='#' and S[x-2]=='#':
        print('No')
        exit()

    unreachable.add(x)    
    if S[x-1]=='.' and ((x-2 in reachable and x-2 not in unreachable) or
                        (x-3 in reachable and x-3 not in unreachable) or
                        (x-1 in reachable and S[x-2]=='.' and S[x]=='.')
    ):
        unreachable.discard(x-1)
    if S[x-2]=='.' and ((x-3 in reachable and x-3 not in unreachable) or
                        (x-4 in reachable and x-4 not in unreachable)):
        unreachable.discard(x-2)
        
out = 'Yes' if D-1 in reachable and D-1 not in unreachable else 'No'
print(out)

# ##..#..
# #######
# S##.#..
# .#.##..
# #######
# .#..##.
# .#..#.#


 # #.S#.#...#.#...
 # .U.#.#...#.#...
 # ..##.#...#.#...
 # ###############
 # ...###...#.#...
 # ###############
 # ...#.##..#.#...
 # ...#.#.#.#.#...
 # ...#.#..##.#...
 # ###############
 # ...#.#...###...
 # ###############
 # ...#.#...#.##..
 # ...#.#...#.#.#.
 # ...#.#...#.#G.#


