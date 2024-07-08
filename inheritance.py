# parent class / super class / base class

class Animal:
    def speak(self):
        print("Animal is speaking")
    def movement(self):
        print("Animal is moving")

class Duck(Animal):
    def Quack(self):
        print("Duck is quacking")
class Bee(Duck):
    def Buzz(self):
        print("Bee is buzzing")

a = Animal()
d = Duck()
d.speak()
b = Bee()
