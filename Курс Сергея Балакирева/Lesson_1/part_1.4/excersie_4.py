import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        [self.lst_data.append(dict(zip(self.FIELDS, Z.split()))) for Z in data]
    def select(self, a, b):
        return self.lst_data[a : b + 1]

db = DataBase()
db.insert(lst_in)
