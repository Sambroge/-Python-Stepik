class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        if isinstance(module, Module):
            self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if not ((key == 'title' and type(value) is str) or (key in ['practices', 'duration'] and type(value) is int)):
            raise TypeError('Неверный тип присваиваемых данных.')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item in ['title', 'practices', 'duration']:
            return None
        super().__delattr__(item)

    def __getattr__(self, item):
        if item not in ['title', 'practices', 'duration']:
            return False
        return super().__getattr__(item)
