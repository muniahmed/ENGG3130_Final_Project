import random

def randomMove():
    k = random.randint(0, 2)
    if k == 1:
        move = "C"
    elif k == 2:
        move = "D"

    return move


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

