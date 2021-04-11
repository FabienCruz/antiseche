---
title: Créer un site avec Flask et SQLAlchemy
status: draft
date: 21-03-2021
---

## Tutoriels et documentation

[Real Python - Part1](https://realpython.com/flask-connexion-rest-api/)

[Real Python - Part2](https://realpython.com/flask-connexion-rest-api-part-2/)

[Real Python - Part3](https://realpython.com/flask-connexion-rest-api-part-3/)

[Real Python - Part4](https://realpython.com/flask-connexion-rest-api-part-4/)

[openclassroom - concevez un site avec flask](https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask)

[site officiel flask-sqlachemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Charger les librairies

pour vérifier ce qui est déjà installé:

    pip3 freeze

installer Flask

    pip3 install flask

dans le fichier python

    from flask import Flask

installer SQLAlchemy pour flask

    pip3 install flask-sqlalchemy

dans le fichier python

    from flask-sqlalchemy import SQLAlchemy

## Créer une application flask

[site officiel flask](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World!'

    if __name__ = '__main__':
        app.run()

dans le terminal

    python3 nom_du_fichier.py

## Connecter une base de données avec SQLAlchemy

[site officiel SQLAlchemy](https://www.sqlalchemy.org/)

ci-dessous avec une base postgreSQL nommée 'example', logée sur l'ordinateur local, accessible à l'utilisateur 'macbook', création d'une table 'Person' avec deux données 'id' et 'name'.  
SQLAlchemy permet de se connecter avec différents types de bases de données (PostgreSQL, SQlite, MySQL - MariaDB, Microsoft SQL Server)  

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://macbook@localhost:5432/example'
    db = SQLAlchemy(app)

    class Person(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(), nullable=False)

        def __repr__(self):
        return f"Person ID: { self.id }, name: {self.name }"

    db.create_all()

    @app.route('/')
    def index():
        person = Person.query.first()
        return 'Hello ' + person.name

    if __name__ == '__main__':
        app.run()

### Manipuler des données avec SQLAlchemy

[une cheat sheet](https://video.udacity-data.com/topher/2019/August/5d5a52af_query-cheat-sheet/query-cheat-sheet.pdf)

#### Ajouter des données

[la documentation officielle](https://docs.sqlalchemy.org/en/14/orm/session.html)

en utilisant la classe Person de l'exemple précédent

    person = Person(name = 'Jean-Marc')
    db.session.add(person)
    db.session.commit()

#### Lire des données

[la documentation officielle](https://docs.sqlalchemy.org/en/14/orm/loading_objects.html)

    Person.query.first()
    Person.query.all()
    Person.query.filter_by(name = 'Jean-Marc').all()
    Person.query.count()

    session.query(Person)

#### Supprimer des données

    Person.query.filter_by(name = 'Jean-Marc').delete()

## Ajouter flask-migrate

Flask-Migrate est une extension qui gère les changements sur les bases de données gérées avec SQLAlchemy

[la documentation officelle](https://flask-migrate.readthedocs.io/en/latest/) contient un exemple très simple à suivre.