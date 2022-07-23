class Shop:
    def __init__(self, title):
        self.title = title
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    identificator = 0

    def __new__(cls, *args, **kwargs):
        cls.identificator += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.identificator

    def __setattr__(self, key, value):
        if not ((key == 'name' and type(value) is str) or (key in ['weight', 'price'] and type(value) in [float, int] and value >= 0) or (key == 'id' and type(value) is int)):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(item)
