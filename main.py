from dataclasses import dataclass
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

    


class Patient22:
    def __init__(self, id:int, namn:str, age:int):
        self.__id = id
        self.__namn = namn
        self.Age = 0
        self.Age = age
    
    def getNamn(self):
        return self.__namn

    def setNamn(self, newValue):
        if len(newValue) < 2:
            print("För kort")
        else:
            self.__namn = newValue

    
    @property        
    def Age(self):
        return self._age
    
    @Age.setter
    def Age(self, newValue):
        if newValue > 0 and newValue < 150:
            self._age = newValue


p3 = Patient22(12, "Stefan",-45)
print(p3.setNamn("Stefan1"))
print(p3.getNamn())
#p3.setAge(23)
p3.age = 23

p3.age = p3.age  + 1
#p3.setAge(p3.getAge() + 1)






@dataclass
class Patient:
    Id :int
    Namn: str
    Age: int
    City: str
    Postnr: str

p = Patient(22, "Stefan Holmberg", 50, "ewer","11122")
p2 = Patient(22, "Stefan Holmberg", 50, "ewer", "11122")
if p == p2: # SKA BLI SANT
    print("Japp det är samma person") # todo add "Id"
else:
    print("Inte samma person")    


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
k.Add(Patient("Stefan",10))
k.Add(Patient("kalle",20))
k.Add(Patient("lisa",30))
p = k.GetNext() # p.Namn = "Stefan"

k = OurStack()  # class OurStack ska ni skapa
k.Add(Patient("Stefan",10))
k.Add(Patient("kalle",20))
k.Add(Patient("lisa",30))
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
    
