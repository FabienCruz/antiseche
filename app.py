import pathlib, glob, re, markdown, datetime
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField
from wtforms.validators import AnyOf, InputRequired, Length, Regexp
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

#--------------------------
# Database
#--------------------------
client = MongoClient()
db = client.cheatsheet
sheets = db.sheet

#--------------------------
# Form
#--------------------------

class Form(FlaskForm):
    title = StringField('titre')
    file = StringField('fichier', validators=[InputRequired(), Length(min=3, max=20, message='doit avoir entre 3 et 20 caractères'), Regexp(r'^[\w]+$', message="uniquement alphanumérique et sans espace")])
    date = DateTimeField('date')
    draft = StringField('brouillon', default="True", validators=[InputRequired(), AnyOf(['True', 'False'])])
    text = TextAreaField('texte')

#--------------------------
# Routes
#--------------------------

@app.route('/')
def index():
    return redirect(url_for('show_list', draft="False"))

@app.route('/sheet/<id>')
def open_file(id):
    sheet = sheets.find_one({"_id": ObjectId(id)})
    content = markdown.markdown(sheet['content'])
    return render_template('sheet.html', title=sheet['title'], date=sheet['date'], content=content)

@app.route('/sheet/new', methods=['GET'])
def new():
    form = Form()
    return render_template('form.html', form=form)

@app.route('/sheet/new', methods=['POST'])
def new_submission():
    form = Form(meta={'csrf': False})
    new_document = {}
    new_document['title'] = form.title.data
    new_document['draft'] = form.draft.data
    new_document['date'] = datetime.datetime.now()
    new_document['content'] = form.text.data
    sheets.insert_one(new_document)
    return redirect(url_for('index'))

@app.route('/sheet/<id>', methods=['DELETE'])
def delete(id):
    sheets.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('show_list', draft=True))

@app.route('/sheets/<draft>')
def show_list(draft):
    print(draft)
    files = []
    for file in sheets.find({'draft': draft}, {'title': 1}):
        files.append(file)
    #for file in sheets.find():
    #    files.append(file)
    print(files)
    return render_template('list.html', files=files)

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