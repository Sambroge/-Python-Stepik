class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
class Bag:
    def __init__(self, max_weight):
        self.__things = []
        self.max_weight = max_weight
        self.weight_in_bag = 0
        
    def add_thing(self, thing):
        if self.weight_in_bag + thing.weight <= self.max_weight:
            self.__things.append(thing)
            self.weight_in_bag += thing.weight

    def remove_thing(self, indx):
        self.__things.pop(indx)  
        
    def get_total_weight(self):
        return sum([i.weight for i in self.__things])
    
    @property
    def things(self):
        return self.__things
