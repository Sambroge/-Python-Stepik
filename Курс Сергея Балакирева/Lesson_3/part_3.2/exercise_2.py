class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file_name):
        return file_name[file_name.find('.') + 1:] in self.extensions
