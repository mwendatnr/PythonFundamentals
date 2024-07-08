class Animal :
    def __init__(self,type,hasscales,haswings,colour):
        self.type = type
        self.hasscales = hasscales
        self.haswings = haswings
        self.colour = colour
    def movement(self):
        print(self.type,"is moving")
animal1 = Animal("fish",True,False,"brown")
animal1.movement()
print(animal1.type,animal1.hasscales,animal1.haswings,animal1.colour)
animal2 = Animal("bird",True,True,"white")
animal1 = Animal("fish",False,False,"brown")
