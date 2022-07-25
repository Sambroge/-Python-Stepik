class Model:
    def __init__(self):
        self.flag = False
        self.data = None

    def query(self, *args, **kwargs):
        self.data = kwargs
        self.flag = True

    def __str__(self):
        if not self.flag:
            return 'Model'
        return f'Model: ' + ', '.join([f'{i} = {self.data[i]}' for i in self.data])
