import random


class RandomPassword:
    def __init__(self, pw_chars, min_length, max_length):
        self.pw_chars = pw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join([random.choice(self.pw_chars) for i in range(random.choice([self.min_length, self.max_length]))])


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(3)]
