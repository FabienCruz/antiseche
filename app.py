import pathlib, glob, re, markdown, markupsafe
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

directory = pathlib.Path.cwd() / 'contents/'
files = list(directory.glob('*.md'))

#--------------------------
# Form
#--------------------------
# https://www.youtube.com/watch?v=vzaXBm-ZVOQ
# https://www.youtube.com/watch?v=jR2aFKuaOBs
# https://www.youtube.com/watch?v=VrH0eH4nE-c
# https://www.youtube.com/watch?v=J9O0v-iM0TE
# https://www.youtube.com/watch?v=Frb0NXe1IHw

class DocForm(FlaskForm):
    doc_title = StringField('doc_title')
    doc_file = StringField('doc_file')
    doc_date = DateTimeField('doc_date')
    doc_draft = BooleanField('doc_draft')
    doc_text = TextAreaField('doc_text')

#--------------------------
# Routes
#--------------------------

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/<file_selected>')
def open_file(file_selected):
    file_selected = directory / file_selected
    file_text = parse_text(file_selected.read_text())
    file_title = file_text['title']
    file_date = file_text['date']
    content = markdown.markdown(file_text['content'])
    return render_template('index.html', files=files, title=file_title, date=file_date, content=content)

def parse_text(content):
    body = {}
    # parse front-matter (between "---") and store key, value in body
    fm_glob = re.split("-{3}", content)
    fm_dtl = re.findall(".*:.*", fm_glob[1])
    for item in fm_dtl:
        item_dtl = re.split(":", item)
        body[item_dtl[0]] = item_dtl[1].strip()
    # store text in body
    body['content'] = fm_glob[-1].strip()
    return body

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = DocForm()

    if form.validate_on_submit():
        test = form.doc_text.data
        print(test)
    return 'the text is {}. <p>'.format(form.doc_text.data)
    
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

'''
--------------------------
 TO DO
--------------------------

--create a mini-cms with flask WTF

create file
pick-up file in a list
delete file
read file 
modify file
differenciate draft and publish
show only publish

--create access and authorization

--deploy

--create another version with a postgresql database
'''