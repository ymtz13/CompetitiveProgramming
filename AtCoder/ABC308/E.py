N = int(input())
A = list(map(int, input().split()))
S = input()

tm = [0, 0, 0]
tx = [0, 0, 0]
TM = [tm]
TX = [tx]

for a, c in zip(A, S):
    tm = tm[:]
    tx = tx[:]

    if c == "M":
        tm[a] += 1
    if c == "X":
        tx[a] += 1

    TM.append(tm)
    TX.append(tx)

txN = TX[-1]

ans = 0
for i, (a, c) in enumerate(zip(A, S), 1):
    if c != "E":
        continue

    tm = TM[i - 1]
    tx = [vN - vi for vN, vi in zip(txN, TX[i])]

    for al in range(3):
        for ar in range(3):
            s = {a, al, ar}

            mex = 3
            if 2 not in s:
                mex = 2
            if 1 not in s:
                mex = 1
            if 0 not in s:
                mex = 0

            if mex == 0:
                continue

            cnt = tm[al] * tx[ar]
            ans += cnt * mex

print(ans)
