from jinja2 import Environment, FileSystemLoader
import pathlib, glob, re
import file, markdown

# récupérer la liste des fichiers
def list_files(self):
    list_f = list(self.directory.path.glob('*.md'))
    file_obj = file.File(list_f[0])
    file_content = get_file_content(list_f[0])
    file_dict = dict_file(file_obj, file_content)
    file_content = turn_to_html(file_dict['text'])
    generate_html_file(list_f, file_content)
    # faire une boucle avec la liste des fichiers
    #for f in list_f:
    #    print(f)

# récupérer le contenu d'un fichier
def get_file_content(file_selected):
    return file.File(file_selected).full_path.read_text()

def dict_file(file_obj, file_content):
    file_d = file_obj.parse_body(file_content)
    file_d["name"]= file_obj.full_path.stem
    return file_d

def turn_to_html(text):
    return markdown.markdown(text)

def generate_html_file(files, file_content):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.getgst_template('page.html')
    output = template.render(files=files, content=file_content)
    print(output)


# corriger navigation
# enregistrer un html
# générer un fichier index.html

"""
def publish(self):
    if self.publish_value.get() == 'draft':
        return service.info("Le fichier est un brouillon (case à cocher)")
    else:
        content = self.html_content()
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('page.html')
        output = template.render(content=content)
        self.html_file(output)

def html_file(self, content):
    dir = file.Directory('docs/')
    n_file = file.File.normalize_filename('.html')
    nw_file = dir.path / n_file
    nw_file.write_text(content)

def html_content(self):
    new_file = self.create_file()
    return markdown.markdown(new_file.body['text'])
"""