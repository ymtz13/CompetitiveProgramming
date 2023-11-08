N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

scores = []
remains = []
for i, s in enumerate(S, 1):
    score = i
    r = []
    for c, a in zip(s, A):
        if c == "o":
            score += a
        else:
            r.append(a)

    scores.append(score)
    remains.append(sorted(r, reverse=True))

ans = []
for i, (score, remain) in enumerate(zip(scores, remains)):
    ss = scores[:]
    ss[i] = 0
    max_score = max(ss)

    cnt = 0
    for v in remain:
        if score >= max_score:
            break
        score += v
        cnt += 1

    ans.append(cnt)

for a in ans:
    print(a)
