class Clock:
    def __init__(self, time=0):
        self.__time = time
    
    
    def set_time(self, tm):
        if Clock.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time
    
    @classmethod
    def __check_time(cls, tm):
        return type(tm) in (int, ) and 0 <= tm <= 100_000
    
    
clock = Clock()
clock.set_time(4530)
