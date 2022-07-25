class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.func(input())]


@InputDigits
def input_dg(string):
    return string.split()


res = input_dg()
