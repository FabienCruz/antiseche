---
title: Créer des formulaires avec flask_wtf
draft: True
date: 14-05-2021
---


## Tutoriels:

2 tutoriels de 10 min. chacun :

- [introduction à flask_wtf](https://www.youtube.com/watch?v=vzaXBm-ZVOQ)
- [valider le contenu des champs](https://www.youtube.com/watch?v=jR2aFKuaOBs)
- [faire des macro pour répéter un schéma étiquette / champ / erreur](https://www.youtube.com/watch?v=J9O0v-iM0TE)

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeField

class Form(FlaskForm):
    title = StringField('title')
    file = StringField('file')
    date = DateTimeField('date')
    draft = BooleanField('draft')
    text = TextAreaField('text')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = Form()

    if form.validate_on_submit():
        test = form.text.data
        print(test)
    return render_template('form.html', form=form)

<form method="POST" action="{{ url_for('form') }}">
    {{ form.csrf_token }}
    {{ form.title }}
    {{ form.title.label }}
    {{ form.text(rows="10", cols="150") }}
    {{ form.date }}
    {{ form.date.label }}
    {{ form.draft }}
    {{ form.draft.label }}
    {{ form.file }}
    {{ form.file.label }}
    <input type="submit" value="Créer">
</form>