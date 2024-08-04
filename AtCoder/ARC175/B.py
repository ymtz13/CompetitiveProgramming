N, A, B = map(int, input().split())
S = [1 if c == "(" else -1 for c in input()]
IS = list(enumerate(S))

nP = len([c for c in S if c == 1])
nQ = 2 * N - nP

D = N - nP
if D >= 0:
    cnt = 0
    for i, c in IS:
        if cnt == D:
            break
        if c == -1:
            S[i] = 1
            cnt += 1
else:
    D = -D
    cnt = 0
    for i, c in IS[::-1]:
        if cnt == D:
            break
        if c == +1:
            S[i] = -1
            cnt += 1

iP = [i for i, c in enumerate(S) if c == 1][::-1]
iQ = [i for i, c in enumerate(S) if c == -1]


def f(tgt):
    SS = S[:]
    for ip, iq in zip(iP[:tgt], iQ[:tgt]):
        if ip < iq:
            return True

        SS[ip] = -1
        SS[iq] = +1

    acc = 0
    for c in SS:
        acc += c
        if acc < 0:
            return False

    return True


ok = N
ng = -1
while ok - ng > 1:
    tgt = (ok + ng) // 2
    if f(tgt):
        ok = tgt
    else:
        ng = tgt

print(D * B + min(A, B * 2) * ok)
