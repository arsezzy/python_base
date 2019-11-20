#!/usr/bin/python3

class Cell():

    def __init__(self, nucleus):
        self.nucleus = nucleus

    @property
    def nucleus(self):
        return self.__nucleus

    @nucleus.setter
    def nucleus(self, nucleus):
        if nucleus <= 0:
            raise Exception ("Nucleus in cell must be positive")
        self.__nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        result = self.nucleus - other.nucleus
        return Cell(result)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(round(self.nucleus / other.nucleus))

    def make_order(self, number):
        result = ""
        for i in range(self.nucleus // number):
            result += "*" * number + "\n"
        result += "*" * (self.nucleus % number)
        return result


try:
    cell1 = Cell(21)
    cell2 = Cell(2)
    print(f"Cell1 has {cell1.nucleus} nucleas, " 
          f"cell2 has {cell2.nucleus} nucleas")
    cell3 = cell1 + cell2
    print(f"Sum of cell1 and cell2 is {cell3.nucleus}")
    cell4 = cell1 - cell2
    print(f"Substract of cell1 and cell2 is {cell4.nucleus}")
    cell5 = cell1 * cell2
    print(f"Multiplication of cell1 and cell2 is {cell5.nucleus}")
    cell6 = cell1 / cell2
    print(f"division of cell1 and cell2 is {cell6.nucleus}")
except Exception:
    print("Nucleus in cell must be positive!")

order = 5
print(f"Order for cell1 with {order} is \n" + cell1.make_order(order))

