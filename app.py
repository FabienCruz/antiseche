import pathlib, glob, re, markdown, datetime
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField
from wtforms.validators import InputRequired, Length, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

directory = pathlib.Path.cwd() / 'contents/'
files = list(directory.glob('*.md'))

#--------------------------
# Class
#--------------------------

class Document():
    def __init__(self, name):
        self.name = name
        self.path = pathlib.Path.cwd() / 'contents/' / name
        self.body = {}

    def save_md(self):
        document = """---\ntitle: {}
        \ndraft: {}
        \ndate: {}
        \n---
        \n{}""".format(self.body['title'], 
        self.body['draft'], 
        self.body['date'],
        self.body['content'])
        return self.path.write_text(document)

    def parse(self):
        document = self.path.read_text()
        # parse front-matter (between "---") and store key, value in body
        fm_glob = re.split("-{3}", document)
        fm_dtl = re.findall(".*:.*", fm_glob[1])
        for item in fm_dtl:
            item_dtl = re.split(":", item)
            self.body[item_dtl[0]] = item_dtl[1].strip()
        # store text in body
        self.body['content'] = fm_glob[-1].strip()
        return self.body

class Form(FlaskForm):
    title = StringField('titre')
    file = StringField('fichier', validators=[InputRequired(), Length(min=3, max=20, message='doit avoir entre 3 et 20 caractères'), Regexp(r'^[\w]+$', message="uniquement alphanumérique et sans espace")])
    date = DateTimeField('date')
    draft = BooleanField('brouillon', default="checked")
    text = TextAreaField('texte')

#--------------------------
# Routes
#--------------------------

@app.route('/')
def index():
    files = list(directory.glob('*.md'))
    return render_template('list.html', files=files)

@app.route('/<file_selected>')
def open_file(file_selected):
    document = Document(file_selected).parse()
    content = markdown.markdown(document['content'])
    return render_template('sheet.html', files=files, title=document['title'], date=document['date'], content=content)

@app.route('/new', methods=['GET'])
def new():
    form = Form()
    return render_template('form.html', form=form)

@app.route('/new', methods=['POST'])
def new_submission():
    form = Form(meta={'csrf': False})
    name = "{}.md".format(form.file.data)
    new_document = Document(name)
    new_document.body['title'] = form.title.data
    new_document.body['draft'] = form.draft.data
    new_document.body['date'] = datetime.datetime.now()
    new_document.body['content'] = form.text.data
    new_document.save_md()
    return redirect(url_for('open_file', file_selected=name))

if __name__ == '__main__':
    app.debug=True
    app.run()

'''
--------------------------
 TO DO
--------------------------

--create a mini-cms with flask WTF

pick-up file in a list
read file 
create file
differenciate draft and publish
show only publish
modify file
delete file

--create access and authorization

--deploy

--create another version with a postgresql database / mongodb
'''