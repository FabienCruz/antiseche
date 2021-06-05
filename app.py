import pathlib, glob, re, markdown, datetime
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField
from wtforms.validators import InputRequired, Length, Regexp
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
    draft = BooleanField('brouillon', default="checked")
    text = TextAreaField('texte')

#--------------------------
# Routes
#--------------------------

@app.route('/')
def index():
    files = []
    for file in sheets.find({}, {'title': 1}):
        files.append(file)
    return render_template('list.html', files=files)

@app.route('/<id>')
def open_file(id):
    sheet = sheets.find_one({"_id": ObjectId(id)})
    content = markdown.markdown(sheet['content'])
    return render_template('sheet.html', title=sheet['title'], date=sheet['date'], content=content)

@app.route('/new', methods=['GET'])
def new():
    form = Form()
    return render_template('form.html', form=form)

@app.route('/new', methods=['POST'])
def new_submission():
    form = Form(meta={'csrf': False})
    new_document = {}
    new_document['title'] = form.title.data
    new_document['draft'] = form.draft.data
    new_document['date'] = datetime.datetime.now()
    new_document['content'] = form.text.data
    sheets.insert_one(new_document)
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['DELETE'])
def delete():
    #écrire eventlistener en javascript dans la page
    sheets.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

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