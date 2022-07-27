class SoftList(list):
    def __init__(self, thing):
        self.thing = list(thing)

    def __getitem__(self, item):
        if (item > -1 and item > len(self.thing) - 1) or (item < 0 and abs(item) > len(self.thing)):
            return False
        return self.thing[item]
