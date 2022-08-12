lowestgradelist = []
finallist = []
scores = []
for c in range(int(input())):
    name = input()
    score = float(input())
    finallist.append([name, score])
    scores.append(score)
settedscores = sorted(list(set(scores)))
sortedscores = sorted(settedscores)
secondlowest = sortedscores[1]
for pos in finallist:
    if pos[1] == secondlowest:
        lowestgradelist.append(pos[0])
for name in sorted(lowestgradelist):
    print(name)