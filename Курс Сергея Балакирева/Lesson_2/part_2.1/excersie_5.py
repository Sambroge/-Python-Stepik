class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y
    
class Rectangle:
    def __init__(self, x1, y1, x2=0, y2=0):
        self.__sp = Point(x1, y1) if type(x1) in [int, float] else x1 
        self.__ep = Point(x2, y2) if type(y1) in [int, float] else y1 
        
    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep
        
    def get_coords(self):
        return (self.__sp, self.__ep)
    
    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')
        
rect = Rectangle(0, 0, 20, 34)
