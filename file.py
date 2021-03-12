import pathlib, glob, re

class Directory:
  def __init__(self, path):
    self.path = pathlib.Path.cwd() / path
  
  def list_files(self, extension):
    self.files = []
    for f in list(self.path.glob('*{}'.format(extension))):
        self.files.append(f.stem)
    return self.files
 
class File:
  def __init__(self, full_path):
    self.full_path = full_path

  def parse_body(self, content):
    self.body = {}
    # parse front-matter (between "---") and store key, value in body
    self.fm_glob = re.split("-{3}", content)
    self.fm_dtl = re.findall(".*:.*", self.fm_glob[1])
    for item in self.fm_dtl:
        self.item_dtl = re.split(":", item)
        self.body[self.item_dtl[0]] = self.item_dtl[1].strip()
    # store text in body
    self.body['text'] = self.fm_glob[-1].strip()
    return self.body
  
  def normalize_filename(self, name, exts):
    normalized_name = re.sub("\s", "-", name.strip())
    file_name = "{}{}".format(normalized_name, exts)
    return file_name

  def save_file(self, directory, name, extension, content):
    file_name = File.normalize_filename(self, name, extension)
    file_name = directory.path / file_name
    file_name.write_text(content)
    

    