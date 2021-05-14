import pathlib, glob, re, markdown, markupsafe
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField

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
    title = StringField('title')
    file = StringField('file')
    date = DateTimeField('date')
    draft = BooleanField('draft')
    text = TextAreaField('text')

#--------------------------
# Routes
#--------------------------

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/<file_selected>')
def open_file(file_selected):
    document = Document(file_selected).parse()
    content = markdown.markdown(document['content'])
    return render_template('sheet.html', files=files, title=document['title'], date=document['date'], content=content)

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = Form()

    if form.validate_on_submit():
        test = form.text.data
        print(test)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

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