class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.checker(obj):
            self.__next = obj
        
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj
        
    def checker(self, obj):
        return isinstance(obj, StackObj) or obj is None
    
class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        
    def push(self, obj):# - добавление объекта класса StackObj в конец односвязного списка;
        if self.top is None:
            self.top = obj
            self.last = obj
        else:
            self.last.next = obj
            self.last = obj
        
    def pop(self): # - извлечение последнего объекта с его удалением из односвязного списка;
        if self.top == self.last:
            self.top = self.last = None
            return None
        finder = self.top
        while finder and finder.next:
            finder = finder.next
            if finder.next:
                self.last = finder
        self.last.next = None
        
    
    def get_data(self):
        array = []
        self.last = self.top
        if not self.last:
            return array
        while self.last.next:
            array.append(self.last.data)
            self.last = self.last.next
        return array + [self.last.data]
