import random

class OurQueue:
    def __init__(self):
        self.__listan = []
    def Add(self, p):
        self.__listan.append(p)
    def GetNext(self):
        if len(self.__listan) == 0:
            return None
        item = self.__listan[0]    
        del self.__listan[0]
        return item


class OurStack:
    def __init__(self):
        self.__listan = []
    def Add(self, p):
        self.__listan.append(p)
    def GetNext(self):
        if len(self.__listan) == 0:
            return None
        item = self.__listan[len(self.__listan)-1]    
        del self.__listan[len(self.__listan)-1]
        return item

    


class Patient:
    def __init__(self, namn:str):
        self.Namn = namn

queuen = []

def NewPatient():
    namn = input("Vad heter patienten:")
    p = Patient(namn)
    queuen.append(p)

def RopaUppNasta():
    a = 123
    b = 2313
    patienten = queuen[0]    
    print("Nästa = " + patienten.Namn)
    del queuen[0]



k = OurQueue()  # class OutQueue ska ni skapa
k.Add(Patient("Stefan"))
k.Add(Patient("kalle"))
k.Add(Patient("lisa"))
p = k.GetNext() # p.Namn = "Stefan"

k = OurStack()  # class OurStack ska ni skapa
k.Add(Patient("Stefan"))
k.Add(Patient("kalle"))
k.Add(Patient("lisa"))
p = k.GetNext() # p.namn = "lisa"





NewPatient()    
NewPatient()
NewPatient()
while True:
    RopaUppNasta()

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
    
