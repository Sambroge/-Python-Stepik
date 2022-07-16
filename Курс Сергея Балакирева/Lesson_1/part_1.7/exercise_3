from re import match
from string import ascii_lowercase as a


class CardCheck:

    @staticmethod
    def check_card_number(number):
        return match('\d{4}-\d{4}-\d{4}-\d{4}', number) is not None

    @staticmethod
    def check_name(name):
        return len(name.split()) == 2 and all([y in a.upper() for i in name.split() for y in i])
