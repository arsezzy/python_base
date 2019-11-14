#!/usr/bin/python3

class Car():
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.turn_on = {"left", "right"}

    def go(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self, direction):
        if direction in self.turn_on:
            print(f"{self.name} turned on {direction}")
        else:
            print("No such direction")

    def show_speed(self):
        print(f"your current speed is {self.speed}")


class TownCar(Car):
    SPEED_LIMIT = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"your current speed is {self.speed}")
        if self.speed > TownCar.SPEED_LIMIT:
            print(f"slow down! Your max speed is {TownCar.SPEED_LIMIT}")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    SPEED_LIMIT = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"your current speed is {self.speed}")
        if self.speed > WorkCar.SPEED_LIMIT:
            print(f"slow down! Your max speed is {WorkCar.SPEED_LIMIT}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


t1 = TownCar(100, "black", "town1")
t2 = TownCar(40, "blue", "town2")
print(t1.is_police)
print(t2.is_police)
t1.show_speed()
t2.show_speed()
t1.turn("left")
t2.turn("forward")
w1 = WorkCar(20, "black", "work1")
w2 = WorkCar(50, "green", "work2")
w1.show_speed()
w2.show_speed()
p1 = PoliceCar(70, "blue", "police1")
print(p1.is_police)
p1.show_speed()

