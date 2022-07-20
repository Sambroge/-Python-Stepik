class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def get_coords(self):
        return tuple(map(lambda x: x[1], self.__dict__.items()))
    
    def draw(self):
        print(' '.join(list(map(lambda x: str(x[1]), self.__dict__.items()))))
