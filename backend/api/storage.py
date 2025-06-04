from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name: str, max_length=None):
        print(name)
        self.delete(name)
        return name