#!/usr/bin/python3

import time
from itertools import cycle
from sys import exit

class TrafficLight():
    __color = None

    def running(self):
        self.index = 0
        self.timers = {"red": 7, "yellow": 2, "green": 5}
        self.order = ["red", "yellow", "green", "yellow"]
        self.next_color = self.order[0]
        for el in cycle(self.order):
            if self.next_color != el:
                exit_code = 1
                print(f"Alarm! Wrong order! Exiting with code {exit_code}")
                exit(exit_code)
            self.__color = el
            print(f"current light is {self.__color}, {time.ctime()}")
            self.index += 1
            self.next_color = self.order[self.index % len(self.order)]
            time.sleep(self.timers[el])


t1 = TrafficLight()
t1.running()

