class Person():
    def __init__(self, number):
        self.identifier = number
        self.fitness = 0
        self.opponent = None
        #self.memory[10] = {}

class Pushover(Person):
    def __init__(self, number):
        Person.__init__(self, number)
        self.type = "Pushover"
        self.strategy = {None: "C", "C": "C", "D": "C"}

class Psycopath(Person):
    def __init__(self, number):
        Person.__init__(self, number)
        self.type = "Psycopath"
        self.strategy = {None: "D", "C": "D", "D": "D"}

def printInfo(people):
    for i in range(0, len(people)):
        print("Person ", people[i].identifier)
        print("Type: ", people[i].type)
        print("Fitness: ", people[i].fitness)
        print("Opponent: ", people[i].opponent.identifier)

def printIndividualInfo(people, identifier):
    for i in range(0, len(people)):
        if people[i].identifier == identifier:
            break

    print("------")
    print("Person: ", people[i].identifier)
    print("Type: ", people[i].type)
    print("Fitness: ", people[i].fitness)
    print("Opponent: ", people[i].opponent.identifier)
    print("------")

def resetFitness(people):
    for i in range(0, len(people)):
        people[i].fitness = 0

def playGame(player1, player2):
    previous1 = None
    previous2 = None
    current1 = None
    current2 = None
    for i in range(0, 5):
        current1 = player1.strategy[previous2]
        current2 = player2.strategy[previous1]
        previous1 = current1
        previous2 = current2
        if current1 == "D" and current2 == "D":
            player1.fitness += 1
            player2.fitness += 1
        elif current1 == "D" and current2 == "C":
            player1.fitness += 3
            player2.fitness += 0
        elif current1 == "C" and current2 == "D":
            player1.fitness += 0
            player2.fitness += 3
        elif current1 == "C" and current2 == "C":
            player1.fitness += 2
            player2.fitness += 2

import random

people = []
psycopathCount = 0
pushoverCount = 0


for i in range(1, 101):
    type = random.randint(1, 2)
    if type == 1:
        person = Pushover(i)
        pushoverCount += 1
    elif type == 2:
        person = Psycopath(i)
        psycopathCount += 1
    people.append(person)

print("Psycopaths: ", psycopathCount)
print("Pushovers: ", pushoverCount)

seen = []
for i in range(1, int(len(people)/2)+1):
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

print(len(seen)," == ",len(people))
print(len(seen) == len(people))
# printInfo(people)

played = []
for i in range(0, len(people)):
    if people[i].identifier not in played:
        playGame(people[i], people[i].opponent)
        played.append(people[i].identifier)
        played.append(people[i].opponent.identifier)
printInfo(people)

printIndividualInfo(people, 6)