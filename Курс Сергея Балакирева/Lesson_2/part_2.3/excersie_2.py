class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_value = min_length
        self.max_value = max_length

    def validate(self, string):
        return type(string) is str and self.min_value <= len(string) <= self.max_value


class StringValue:
    def __init__(self, validator=ValidateString()):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'''<form>
        Логин: {self.login}
        Пароль: {self.password}
        Email: {self.email}
        </form>''')
