class ValName:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if type(value) is str:
            setattr(instance, self.name, value)


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        self.type = set()

    def add_app(self, app):
        if type(app) not in self.type:
            self.type.add(type(app))
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)

class AppVK:
    name = ValName()
    def __init__(self, name='ВКонтакте'):
        self.name = name
        
        
class AppYouTube:
    name = ValName()
    def __init__(self, memory_max, name="YouTube"):
        self.name = name
        self.memory_max = memory_max
    
    
class AppPhone:
    name = ValName()
    def __init__(self, phone_list, name='Phone'):
        self.name = name
        self.phone_list = phone_list
