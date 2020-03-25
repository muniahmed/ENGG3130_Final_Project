import random

def randomMove():
    k = random.randint(0, 2)
    if k == 1:
        move = "C"
    elif k == 2:
        move = "D"

    return move

#if it were to lose a game it would take one move from opponents strategy and make it their own
class Person():
    def __init__(self, number):
        self.identifier = number
        self.totalFitness = 0
        self.roundFitness = 0
        self.opponent = None
        #self.memory[10] = {}
#Change strategys to percentages instead of binary based on previous rounds
class Generous(Person):
    def __init__(self, number):
        Person.__init__(self, number)
        self.type = "Generous"
        self.strategy = {None: 0.9, "C": 0.9, "D": 0.9}

class Selfish(Person):
    def __init__(self, number):
        Person.__init__(self, number)
        self.type = "Selfish"
        self.strategy = {None: 0.1, "C": 0.1, "D": 0.1}

class TitForTat(Person):
    def __init__(self, number):
        Person.__init__(self, number)
        self.type = "Tit For Tat"
        self.strategy = {None: 0.9, "C": 0.9, "D": 0.1}

class randomPerson(Person):
    def __init__(self, number):
        Person.__init__(self, number)
        self.type = "Random"
        self.strategy = {None: randomMove, "C": randomMove, "D": randomMove}

def printInfo(people):
    for i in range(0, len(people)):
        print("Person", people[i].identifier)
        print("Type:", people[i].type)
        print("Strategy: {none:", people[i].strategy[None], ", C:", people[i].strategy["C"], ", D:",
              people[i].strategy["D"], "}")
        print("Fitness:", people[i].totalFitness)
        print()



def printIndividualInfo(people, identifier):
    for i in range(0, len(people)):
        if people[i].identifier == identifier:
            break

    print("------")
    print("Person: ", people[i].identifier)
    print("Type: ", people[i].type)
    print("Fitness: ", people[i].totalFitness, "(",people[i].roundFitness,")")
    print("Strategy: {none:", people[i].strategy[None], ", C:", people[i].strategy["C"], ", D:",
          people[i].strategy["D"], "}")
    print("Opponent: ", people[i].opponent.identifier)
    print("Opponent Type: ", people[i].opponent.type)
    print("Opponent Strategy: {none:", people[i].opponent.strategy[None], ", C:", people[i].opponent.strategy["C"],
          ", D:",
          people[i].opponent.strategy["D"], "}")
    print("------")

def resetFitness(people):
    for i in range(0, len(people)):
        people[i].totalFitness += people[i].roundFitness
        people[i].roundFitness = 0

def playGame(player1, player2):
    minChance = 0.0
    maxChance = 1.0
    previous1 = None
    previous2 = None
    current1 = None
    current2 = None
    for i in range(0, 5):
        rand1 = random.random()
        rand2 = random.random()
        if rand1 >= player1.strategy[previous2]:
            current1 = "D"
        elif rand1 < player1.strategy[previous2]:
            current1 = "C"

        if rand2 >= player2.strategy[previous1]:
            current2 = "D"
        elif rand2 < player2.strategy[previous1]:
            current2 = "C"

        previous1 = current1
        previous2 = current2
        if current1 == "D" and current2 == "D":
            player1.roundFitness += 1
            player2.roundFitness += 1
            player1.strategy[previous2] = min(maxChance, player1.strategy[previous2] + 0.1)
            player2.strategy[previous1] = min(maxChance, player2.strategy[previous1] + 0.1)
        elif current1 == "D" and current2 == "C":
            player1.roundFitness += 3
            player2.roundFitness += 0
            player1.strategy[previous2] = max(minChance, player1.strategy[previous2] - 0.1)
            player2.strategy[previous1] = max(minChance, player2.strategy[previous1] - 0.1)
        elif current1 == "C" and current2 == "D":
            player1.roundFitness += 0
            player2.roundFitness += 3
            player1.strategy[previous2] = max(minChance, player1.strategy[previous2] - 0.1)
            player2.strategy[previous1] = max(minChance, player2.strategy[previous1] - 0.1)
        elif current1 == "C" and current2 == "C":
            player1.roundFitness += 2
            player2.roundFitness += 2
            player1.strategy[previous2] = min(maxChance, player1.strategy[previous2] + 0.1)
            player2.strategy[previous1] = min(maxChance, player2.strategy[previous1] + 0.1)
    return



random.seed(300) #notable seeds: 78 (Generous starts to take advantage of cooperation and defends itself), 300 (Generous turns into a tit for tat),

people = []
selfishCount = 0
generousCount = 0
TFTCount = 0

for i in range(1, 101):
    type = random.randint(1, 3)
    if type == 1:
        person = Generous(i)
        generousCount += 1
    elif type == 2:
        person = Selfish(i)
        selfishCount += 1
    elif type == 3:
        person = TitForTat(i)
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
            playGame(people[k], people[k].opponent)
            played.append(people[k].identifier)
            played.append(people[k].opponent.identifier)
    printIndividualInfo(people, 93)

    resetFitness(people)


printInfo(people)

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