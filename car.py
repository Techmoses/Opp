# Python ENCAPSULATION
class car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
    def set_speed (self, value) :
        self.__speed = value

    def get_speed (self):
        return self.__speed
    def get_color (self, value):
        self.__color = value

    def get_color (self):
        return self.__color

ford = car (200, 'red')
Honda = car (250, 'blue')
Audi = car (300, 'black')

ford.set_speed(500)
print(ford.get_speed())
print(ford.get_color())