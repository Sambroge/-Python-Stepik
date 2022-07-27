class ItemAttrs:
    def __getitem__(self, item):
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__.keys())[key]] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y
