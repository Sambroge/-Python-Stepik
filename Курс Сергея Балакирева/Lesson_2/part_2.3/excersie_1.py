class FloatValue:
    def check_value(self, instance):
        if not type(instance) is float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check_value(value)
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(float(j + n * i)) for j in range(1, n + 1)] for i in range(m)]


table = TableSheet(3, 5)
