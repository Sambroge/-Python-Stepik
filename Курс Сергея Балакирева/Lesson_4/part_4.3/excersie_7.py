class StringDigit(str):
    def __init__(self, string):
        if not self.check_ctring(string):
            raise ValueError("в строке должны быть только цифры")
        self.string = string

    def __add__(self, string):
        if not self.check_ctring(string):
            raise ValueError("в строке должны быть только цифры")
        self.string = self.string + string
        return StringDigit(self.string)

    def __radd__(self, string):
        if not self.check_ctring(string):
            raise ValueError("в строке должны быть только цифры")
        self.string = string + self.string
        return StringDigit(self.string)

    def __str__(self):
        return self.string

    @staticmethod
    def check_ctring(string):
        return string.isdigit()
