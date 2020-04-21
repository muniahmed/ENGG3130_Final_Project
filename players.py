from gameFunctions import randomMove

#if it were to lose a game it would take one move from opponents strategy and make it their own
class Person():
    def __init__(self, number):
        self.identifier = number
        self.totalFitness = 0
        self.roundFitness = 0
        self.opponent = None
        #self.memory[10] = {}
        self.nhist = []
        self.chist = []
        self.dhist = []

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
