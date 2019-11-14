#!/usr/bin/python3

class Worker():
    def __init__(self, name, surname, position, wage = 0, bonus = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def print_name(self):
        print(self.name)


class Position(Worker):
    def __init__(self, name, surname, position, wage = 0, bonus = 0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

pos1 = Position("Steve", "Jobs", "Vice President", 100, 35)
pos2 = Position("Bill", "Gates", "Chairman")
print(pos1.get_full_name())
print(pos1.get_total_income())
print(pos2.get_full_name())
print(pos2.get_total_income())

