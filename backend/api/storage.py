from django.core.files.storage import FileSystemStorage
import os


def get_filepath(instance, filename):
    path = os.path.join(f"user_{instance.id}", f"avatar", filename)
    return path


class ExclusiveStorage(FileSystemStorage):
    def get_available_name(self, name: str, max_length=None):
        full_path = self.path(name)
        directory = os.path.dirname(full_path)
        if not os.path.isdir(directory):
            return name

        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    os.remove(entry)

        name, ext = name.split(".")
        return self.get_alternative_name(name, "." + ext)