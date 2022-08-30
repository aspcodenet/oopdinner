import random

class GameCharacter:
    def __init__(self, namn:str):
        self.Namn = namn
        self.Level = 0
    def MightLevelUp(self):
        pass

class Human (GameCharacter):
    def __init__(self, namn:str):
        super().__init__(namn)
        self.Age = 0

    def Act(self):
        actions = ["tänker", "pratar", "sväljer", "rapar"]
        print(self.Namn + " " +  random.choice(actions))
    def MightLevelUp(self):
        self.Level = self.Level + 1

class Fly (GameCharacter):
    def __init__(self, namn:str):
        super().__init__(namn)

    def Act(self):
        actions = ["surrar", "landar i maten", "flyger"]
        print(self.Namn + " " +  random.choice(actions))


s = Human("Stefan")
k = Human("Kerstin")
f = Fly("Flugan")
gameObjects = [s,k,f]
while True:
    for gameObject in gameObjects:
        gameObject.Act()
        gameObject.MightLevelUp()
    
