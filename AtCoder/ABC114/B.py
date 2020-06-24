S = input()
r=1000
for i in range(len(S)-2):
    r=min(r, abs(753-int(S[i:i+3])))
print(r)
