class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ['ul', 'ol'] else 'ul'

    def __call__(self, lst, *args, **kwargs):
        strings = ''.join(['\n<li>' + i + '</li>' for i in lst])
        return f'<{self.type_list}>' + f'{strings}' + f'\n</{self.type_list}>'
