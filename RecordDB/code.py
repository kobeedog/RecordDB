import uuid
import shutil
from PIL import Image
from django.core.files.storage import FileSystemStorage

class UniqueIdentifier:

    def __init__(self):
        pass

    def generete_uuid(self):
        return uuid.uuid4()

class FileIO:

    def __init__(self):
        pass

    def save_file(self, file):
        fs = FileSystemStorage()
        filename = fs.save("Temp/" + file.name, file)
        ext = str.split(filename, ".")[1]
        unique_file_name = str(UniqueIdentifier().generete_uuid()) + "." + ext
        self.copy_file(filename, unique_file_name)
        img = Imaging(220, 220)
        img.create_thumbnail('RecordDB/static/images/covers/' + unique_file_name, 'RecordDB/static/images/covers/' + unique_file_name)
        return unique_file_name

    def copy_file(self, file_name, unique_file_name):
        shutil.copy2(file_name, 'RecordDB/static/images/covers/' + unique_file_name)

class Imaging:

    def __init__(self, w, h):
        self.size = w, h

    def create_thumbnail(self, in_file, out_file):
        original_image = Image.open(in_file)
        resized_image = original_image.resize(self.size)
        resized_image.save(out_file)