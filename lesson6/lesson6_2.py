#!/usr/bin/python3

class Road():
    THICKNESS = 5
    MASS_PER_1SQSM = 25
    def __init__(self, length, wigth):
        Road._length = length
        Road._wigth = wigth

    def asphalt_mass(self):
        return(self._length*self._wigth*self.MASS_PER_1SQSM*self.THICKNESS)

r1 = Road(1,2)
print(f"neccesary asphalt amount is {r1.asphalt_mass()} ton")
