import uuid
import shutil
from PIL import Image
import urllib
import urllib.request
import urllib.parse
from django.core.files.storage import FileSystemStorage
from RecordDB.models import Configuration

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

class External:

    def __init__(self):
        pass

    def get_tracks(self, artist_name, album_name):
        # get auth keys for Lastfm
        key = ""
        secret = ""
        config_list = Configuration.objects.order_by('-parameter')
        for config in config_list:
            if config.parameter == "last_fm_key":
                key = config.value
            if config.parameter == "last_fm_secret":
                secret = config.value
        resource = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=" + key + "&artist=" + urllib.parse.quote_plus(artist_name) + "&album=" + urllib.parse.quote_plus(album_name)
        with urllib.request.urlopen(resource) as response:
            resource = response.read()
            xml = XmlParser(resource)
            return xml.parse_tracks()

import xml.etree.ElementTree as et
class XmlParser:

    def __init__(self, document):
        self.document = document

    def parse_tracks(self):
        root = et.fromstring(self.document)
        parsed_tracks = []
        for element in root[0]:
            if element.tag == "tracks":
                tracks = element
                for track in tracks:
                    print(track[0].text)
                    parsed_tracks.append(track[0].text)
                return parsed_tracks


