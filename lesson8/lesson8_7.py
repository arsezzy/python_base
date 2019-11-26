#!/usr/bin/python3

class My_complex_class():
    """My own class for complex numbers"""
    def __init__(self, x, y):
        self.real = x
        self.image = y

    def __add__(self, other):
        return My_complex_class(self.real + other.real, self.image + other.image)

    def __mul__(self, other):
        return My_complex_class(self.real * other.real - self.image * other.image, \
                                self.real * other.image + self.image * other.real)

    def __str__(self):
        if self.image >= 0:
            return f"{self.real} + {self.image}j"
        else:
            return f"{self.real} - {abs(self.image)}j"


complex_number1 = My_complex_class(2, 5)
complex_number2 = My_complex_class(3, -10)
print(complex_number1 + complex_number2)
print(complex_number1 * complex_number2)
