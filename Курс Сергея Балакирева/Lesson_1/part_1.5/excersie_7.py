class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Table(Products):
    pass

class TV(Products):
    pass

class Notebook(Products):
    pass

class Cup(Products):
    pass

class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)
        
    def remove(self, indx):
        try:
            self.goods.pop(indx)
        except:
            print('Не сегодня')
            
    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]
    
cart = Cart()
cart.add(TV('Samsung', 3000))
cart.add(TV('Zvezda', 'over-nine-thousand'))
cart.add(Table('IKEA', 1000))
cart.add(Notebook('China-book', 5000))
cart.add(Notebook('USA-book', 5000))
cart.add(Cup('Starbucks', 7000))
