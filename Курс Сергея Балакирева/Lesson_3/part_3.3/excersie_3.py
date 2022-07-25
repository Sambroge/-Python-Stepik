class WordString:
    def __init__(self, string=None):
        self.strings = string

    def __len__(self):
        return len(self.strings.split())

    def __call__(self, indx):
        return self.words(indx)
    
    def words(self, indx):
        return self.strings.split()[indx]

    @property
    def string(self):
        return self.strings

    @string.setter
    def string(self, st):
        self.strings = st
