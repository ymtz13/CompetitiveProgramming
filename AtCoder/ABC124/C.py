S=[int(c) for c in input()]
T=[i%2 for i in range(len(S))]
q=0
for s,t in zip(S,T):
    q+= s!=t
print(min(q,len(S)-q))
