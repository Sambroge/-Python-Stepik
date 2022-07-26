class Ellipse:
    def __init__(self, *args, **kwargs):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def get_coords(self):
        if not len(self.__dict__.values()) == 4:
            raise AttributeError('нет координат для извлечения')
        return tuple(self.__dict__.values())

    def __bool__(self):
        return len(self.__dict__.values()) == 4
    
lst_geom = [Ellipse(), Ellipse(), Ellipse('x1', 'y1', 'x2', 'y2'), Ellipse('x1', 'y1', 'x2', 'y2')]
[i.get_coords() for i in lst_geom if bool(i)]
