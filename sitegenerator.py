from jinja2 import Environment, FileSystemLoader
import pathlib, glob, re
import file, markdown

# récupérer la liste des fichiers
def list_files(self):
    list_f = list(self.directory.path.glob('*.md'))
    nav_items = []
    dir = file.Directory('docs/')

    for f in list_f:
        file_obj = file.File(f)  
        nav_item = tuple((file_obj.full_path.stem, file_dict['title']))
        nav_items.append(nav_item)

    for f in list_f:
        file_obj = file.File(f)
        file_content = get_file_content(file_obj)
        file_dict = file_obj.parse_body(file_content)
        file_content = turn_to_html(file_dict['text'])
        page_content = make_page(nav_items, file_dict, file_content)
        file_html = dir.path / "{}.{}".format(file_obj.full_path.stem,'html')
        file_html.write_text(page_content)
    

def get_file_content(file_selected):
    return file_selected.full_path.read_text()

def turn_to_html(text):
    return markdown.markdown(text)

def make_page(files, file_dict, file_content):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('page.html')
    output = template.render(files=files, file_dict=file_dict, content=file_content)
    return output


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