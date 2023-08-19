N, T, M = map(int, input().split())
E = [[0] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    E[A - 1][B - 1] = E[B - 1][A - 1] = 1


memo = [None] * (1 << 20)


def solve(bits, numOfTeams):
    key = bits * 32 + numOfTeams
    if memo[key] is not None:
        return memo[key]

    pop = [i for i in range(N) if bits & (1 << i)]
    if len(pop) < numOfTeams:
        return 0
    if not pop:
        return 1
    if numOfTeams == 0:
        return 0

    i, *R = pop

    rbits = []
    # bb = bits - (1 << i)
    # print("BGN {:05b}".format(bits), numOfTeams, pop)
    for x in range(1 << len(R)):
        team = [i] + [v for j, v in enumerate(R) if x & (1 << j)]
        isOk = True
        for z, t1 in enumerate(team):
            for t2 in team[z + 1 :]:
                if E[t1][t2]:
                    isOk = False
        if not isOk:
            continue

        rbit = bits - sum([1 << v for v in team])
        rbits.append(rbit)
        # print("    {:05b}".format(rbit), team, numOfTeams - 1)

    retval = 0
    for rbit in rbits:
        add = solve(rbit, numOfTeams - 1)
        retval += add
        # print("    {:05b}".format(rbits), numOfTeams - 1, add, F)

    # print("END {:05b}".format(bits), numOfTeams, retval)

    memo[key] = retval
    return retval


ans = solve((1 << N) - 1, T)
print(ans)
