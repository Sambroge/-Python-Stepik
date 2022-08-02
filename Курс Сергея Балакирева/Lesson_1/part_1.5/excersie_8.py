import sys

# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj
        
    def link(self, obj):
        if isinstance(obj, ListObject):
            self.next_obj = obj

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
array = [head_obj]
for i in lst_in[1:]:
    array.append(ListObject(i))
    array[-2].link(array[-1])
