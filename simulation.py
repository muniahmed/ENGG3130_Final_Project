import random
import gameFunctions
import players

#notable seeds: 78 (Generous starts to take advantage of cooperation and defends itself), 300 (Generous turns into a tit for tat),
random.seed(300)


people = []
selfishCount = 0
generousCount = 0
TFTCount = 0

for i in range(1, 101):
    type = random.randint(1, 3)
    if type == 1:
        person = players.Generous(i)
        generousCount += 1
    elif type == 2:
        person = players.Selfish(i)
        selfishCount += 1
    elif type == 3:
        person = players.TitForTat(i)
        TFTCount += 1
    people.append(person)

print("Selfish: ", selfishCount)
print("Generous: ", generousCount)
print("TitForTat: ", TFTCount)


for i in range(1, 1001):
    print("Round", i)
    seen = []
    for j in range(1, int(len(people)/2)+1):
    #    player1 = random.randint(0, len(people))
    #    player2 = random.randint(0, len(people))

        while(True):
            player1 = random.randint(0, len(people)-1)
            if(player1 not in seen):
                seen.append(player1)
                break
        while(True):
            player2 = random.randint(0, len(people)-1)
            if(player2 not in seen):
                seen.append(player2)
                break

        people[player1].opponent = people[player2]
        people[player2].opponent = people[player1]

    #print(len(seen)," == ",len(people))
    #print(len(seen) == len(people))
    # printInfo(people)

    played = []
    for k in range(0, len(people)):
        if people[k].identifier not in played:
            gameFunctions.playGame(people[k], people[k].opponent)
            played.append(people[k].identifier)
            played.append(people[k].opponent.identifier)
    gameFunctions.printIndividualInfo(people, 93)

    gameFunctions.resetFitness(people)


gameFunctions.printInfo(people)

highestFitness = 0
fittestPersonIndex = 0
stratNone = 0
stratC = 0
stratD = 0
for n in range(0, len(people)):
    stratNone += people[n].strategy[None]
    stratC += people[n].strategy["C"]
    stratD += people[n].strategy["D"]
    if people[n].totalFitness >= highestFitness:
        highestFitness = people[n].totalFitness
        fittestPersonIndex = n

print("Selfish: ", selfishCount)
print("Generous: ", generousCount)
print("TitForTat: ", TFTCount)
print("The winner overall is person", people[fittestPersonIndex].identifier, "with", people[fittestPersonIndex].totalFitness, "points. Type:", people[fittestPersonIndex].type)
print("Winning strategy: {none:", people[fittestPersonIndex].strategy[None], ", C:", people[fittestPersonIndex].strategy["C"],
          ", D:", people[fittestPersonIndex].strategy["D"], "}", )
print("Average strategy: {none:", stratNone/len(people), ", C:", stratC/len(people),
          ", D:", stratD/len(people), "}", )