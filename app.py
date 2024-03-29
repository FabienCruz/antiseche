import markdown, datetime
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, DateTimeField
from wtforms.validators import InputRequired, Length, Regexp
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

#--------------------------
# Database
#--------------------------
client = MongoClient("mongodb+srv://FabTest:DataBaseFabTest@fabtest.vo6ax.mongodb.net/FabTest?retryWrites=true&w=majority")
db = client.cheatsheet
sheets = db.sheet

#--------------------------
# Form
#--------------------------

class Form(FlaskForm):
    title = StringField('titre')
    file = StringField('fichier', validators=[InputRequired(), Length(min=3, max=20, message='doit avoir entre 3 et 20 caractères'), Regexp(r'^[\w]+$', message="uniquement alphanumérique et sans espace")])
    date = DateTimeField('date')
    draft = RadioField('draft', choices=[('True', 'brouillon'), ('False', 'publication')], default='True')
    text = TextAreaField('texte')

#--------------------------
# Utilities
#--------------------------
def get_files(draft):
    files = []
    for file in sheets.find({'draft': draft}, {'title': 1}):
        files.append(file)
    return files

def get_form_datas(form):
    form_data = {}
    form_data['title'] = form.title.data
    form_data['draft'] = form.draft.data
    form_data['date'] = datetime.datetime.now()
    form_data['content'] = form.text.data
    return form_data

#--------------------------
# Routes
#--------------------------

@app.route('/')
def index():
    return redirect(url_for('show_list', draft='False'))

@app.route('/sheet/<id>')
def open_file(id):
    sheet = sheets.find_one({"_id": ObjectId(id)})
    content = markdown.markdown(sheet['content'])
    return render_template('sheet.html', 
    title=sheet['title'], 
    date=sheet['date'], 
    content=content)

@app.route('/sheet/new', methods=['GET'])
def new():
    form = Form(meta={'csrf': False})
    return render_template('form.html', 
    form=form, 
    direction='new',
    btn_value='Créer')

@app.route('/sheet/new', methods=['POST'])
def new_submission():
    form = Form(meta={'csrf': False})
    new_data = get_form_datas(form)
    sheets.insert_one(new_data)
    flash ('the document is created')
    return redirect(url_for('index'))

@app.route('/sheet/update/<id>', methods=['GET'])
def read_to_update(id):
    form = Form(meta={'csrf': False})
    sheet = sheets.find_one({"_id": ObjectId(id)})
    form.title.data = sheet['title']
    form.draft.data = sheet['draft']
    form.text.data = sheet['content']
    direction = 'update'
    return render_template('form.html', 
    form=form, 
    direction=direction,
    id=id,
    btn_value='Modifier')

@app.route('/sheet/update/<id>', methods=['POST'])
def update(id):
    form = Form(meta={'csrf': False})
    new_data = get_form_datas(form)
    sheets.update_one({"_id": ObjectId(id)}, { "$set": new_data})
    flash ('the document is updated')
    return redirect(url_for('index'))

@app.route('/sheet/<id>', methods=['DELETE'])
def delete(id):
    sheet = sheets.find_one({"_id": ObjectId(id)})
    draft = sheet['draft']
    sheets.delete_one({"_id": ObjectId(id)})
    flash ('the document is deleted')
    return redirect(url_for('show_list', draft=draft))

@app.route('/sheets/<draft>', methods=['GET', 'DELETE'])
def show_list(draft):
    files = get_files(draft)
    return render_template('list.html', files=files)

if __name__ == '__main__':
    app.debug=True
    app.run()

'''
--------------------------
 TO DO
--------------------------

--create a mini-cms with flask WTF

x pick-up file in a list
x read file 
x create file
x differenciate draft and publish
x show only publish
x delete file
x modify file

--create access and authorization

--deploy
'''