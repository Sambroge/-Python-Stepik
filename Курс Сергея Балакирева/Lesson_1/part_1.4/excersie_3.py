import sys

class StreamData:
    def create(self, FIELDS, lst_in):
        if len(FIELDS) == len(lst_in):
            self.id = lst_in[0]
            self.title = lst_in[1]
            self.pages = lst_in[2]
            return True
        return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
