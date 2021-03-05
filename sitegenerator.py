from jinja2 import Environment, FileSystemLoader
import pathlib, glob, re
import file, markdown

# récupérer la liste des fichiers
def list_files(self):
    list_f = list(self.directory.path.glob('*.md'))
    for f in list_f:
        print(f)
# faire une boucle avec la liste des fichiers
# récupérer le contenu d'un fichier
# utiliser la fonction parse_body pour créer un dictionnaire file
# ajouter le nom du fichier au dictionnaire et le lien url
# générer un fichier page.html et navigation html
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