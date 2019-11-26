#!/usr/bin/python3

class Warehouse:
    PRINTER = "Printer"
    SCANER = "Scaner"
    COPYMACHINE = "Copymachine"
    types = [PRINTER, SCANER, COPYMACHINE]
    __equipment = dict((t, []) for t in types)
    @staticmethod
    def receive_equipment(equip):
        for device, params in equip.items():
            if device == Warehouse.PRINTER:
                Warehouse.__equipment[device].append(Printer(params))
            elif device == Warehouse.SCANER:
                Warehouse.__equipment[device].append(Scaner(params))
            elif device == Warehouse.COPYMACHINE:
                Warehouse.__equipment[device].append(CopyMachine(params))
            else:
                print("No such type of equipment!")
        return Warehouse.__equipment

    @staticmethod
    def send_equipment(device_type, serial_number):
        device_deleted = False
        try:
            for device in Warehouse.__equipment[device_type]:
                if device.serial == serial_number:
                    Warehouse.__equipment[device_type].remove(device)
                    print("Equipment was sent!")
                    device_deleted = True
                    break
        except KeyError:
            print("No such type of equipment is existed")
        if not device_deleted:
            print(f"no {serial_number} serial number for {device_type}")
        return Warehouse.__equipment


class OfficeEquipment(Warehouse):
    quantity = 0

    def __init__(self, params):
        self.firm, self.model, self.serial = params[0:3]


class Printer(OfficeEquipment):
    def __init__(self, params):
        super().__init__(params[0:3])
        self.iscolor = params[3]
        Printer.quantity += 1

    def __str__(self):
        return f"{Warehouse.PRINTER} has params: {self.firm}, {self.model}, {self.serial}, {self.iscolor}"


class Scaner(OfficeEquipment):
    def __init__(self, params):
        super().__init__(params[0:3])
        self.dpi = params[3]
        Scaner.quantity += 1

    def __str__(self):
        return f"{Warehouse.SCANER} has params: {self.firm}, {self.model}, {self.serial}, {self.dpi}"


class CopyMachine(OfficeEquipment):
    def __init__(self, params):
        super().__init__(params[0:3])
        self.pages_per_minute = params[3]
        CopyMachine.quantity += 1

    def __str__(self):
        return f"{Warehouse.COPYMACHINE} has params: {self.firm}, {self.model}, {self.serial}, {self.pages_per_minute}"


s1 = {"Scaner": ["Sony", "model1", "123qwer", "300"]}
s2 = {"Scaner": ["Sony", "model2", "456qwe", "400"]}
s3 = {"Scaner": ["Sony", "model3", "789qwe", "500"]}
p1 = {"Printer": ["Samsung", "first", "11111", True]}
p2 = {"Printer": ["HP", "second", "22222", True]}
p3 = {"Printer": ["Sony", "third", "33333", False]}
c1 = {"Copymachine": ["Xerox", "third", "33333", 100]}
Warehouse.receive_equipment(s1)
Warehouse.receive_equipment(s2)
Warehouse.receive_equipment(s3)
Warehouse.receive_equipment(p1)
Warehouse.receive_equipment(p2)
Warehouse.receive_equipment(p3)
w1 = Warehouse.receive_equipment(c1)
for device_type in w1.values():
    for el in device_type:
        print(el)
print("---------------")
w1 = Warehouse.send_equipment("Scaner", "456qwe")
print("---------------")
for device_type in w1.values():
    for el in device_type:
        print(el)

