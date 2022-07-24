class DigitRetrieve:
    def __call__(self, string):
        return int(string) if string.isdigit() or (string[0] == '-' and string[1:].isdigit()) else None

