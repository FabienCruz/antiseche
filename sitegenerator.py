from jinja2 import Environment, FileSystemLoader
import pathlib, glob, re
import file, markdown

def list_files(self):
    list_f = list(self.directory.path.glob('*.md'))
    files_dict = []

    for f in list_f:
        file_obj = file.File(f)
        file_content = get_file_content(file_obj)
        file_dict = file_obj.parse_body(file_content)
        file_dict['text'] = turn_to_html(file_dict['text'])
        file_dict['name'] = file_obj.full_path.stem
        files_dict.append(file_dict)
    
    return files_dict

def get_file_content(file_selected):
    return file_selected.full_path.read_text()

def turn_to_html(text):
    return markdown.markdown(text)

def make_page(navlist, content):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('page.html')
    output = template.render(navlist = navlist, content = content)
    return output

def generate(self):
    files_dict = list_files(self)
    files_dir = file.Directory('docs/')
    for f in files_dict:
        if f['status'] == 'publish':
            page_content = make_page(files_dict, f)
            file_html = files_dir.path / "{}.{}".format(f['name'],'html')
            file_html.write_text(page_content)