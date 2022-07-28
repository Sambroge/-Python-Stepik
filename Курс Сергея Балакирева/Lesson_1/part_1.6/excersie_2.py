class SingletonFive:
    counter = 5
    link = ''
    def __new__(cls, *args, **kwargs):
        if cls.counter:
            cls.counter -= 1
            cls.link = super().__new__(cls)
        return cls.link
    
    def __init__(self, name):
        self.name = name
        
        
objs = [SingletonFive(str(n)) for n in range(10)]
