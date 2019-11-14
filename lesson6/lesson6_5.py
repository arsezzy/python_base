#!/usr/bin/python3

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("start drawing")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"start drawing by pen named {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"start drawing by pencil named {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"start drawing by handle named {self.title}")


pen1 = Pen("my pen")
pen1.draw()
pencil1 = Pencil("my pencil")
pencil1.draw()
handle1 = Handle("my handle")
handle1.draw()

