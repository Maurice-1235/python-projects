from math import pi


class Cone:
    def __init__(self,radius,length):
        self.radius = radius
        self.length = length
    def getLength(self):
        return self.length
    def getRadius(self):
        return self.radius
    def setLength(self,input):
        self.length = input
    def setRadius(self, input):
        self.radius = input
    def getVolume(self):
        return (self.length  * pi * self.radius ** 2)/3

print (Cone(11,10).getVolume())