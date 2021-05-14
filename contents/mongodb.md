---
title: Utiliser une base de données NoSQL - MongoDB
draft: False
date: 14-05-2021
---
[Real python - introduction to mongodb and python](https://realpython.com/introduction-to-mongodb-and-python/) niveau débutant.

[MongoDB - University](https://university.mongodb.com/courses/M001/about) niveau débutant sur le site officiel MongoDB. 8.5 heures de cours gratuits.

[Udacity - Data wrangling with mongo](https://www.udacity.com/course/data-wrangling-with-mongodb--ud032) Niveau plus avancé. 2 mois. gratuit.

MongoDB propose un service cloud gratuit pour les petits projets: Mongo Atlas.

## Vocabulaire

En MongoDB, une **collection** regroupe des **documents** qui contient des paires de **champ : valeur**.

## Installer Mongodb sur Mac OS

la documentation officielle pour l'installation est [ici] (https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#std-label-osx-prereq)

pour installer avec homebrew:

`brew tap mongodb/brew`

`brew install mongodb-community@4.4`

pour utiliser MongoDB avec le terminal (shell):

`brew services start mongodb-community@4.4`

pour l'arrêter :

`brew services stop mongodb-community@4.4`

## Utiliser mongo shell

[les opérations de bases de la documentation officielle] (https://docs.mongodb.com/manual/reference/mongo-shell/)

mongo shell utilise du code JavaScript plutôt que du SQL.

Pour lancer le terminal: 

`mongo`

voir les bases de données:
`show databases`

`show dbs`

voir la base de données en cours:
`db`

voir les collections
`show collections`

utiliser / créer une base de données (sera créée avec l'ajout du premier document):
`use <nom_de_la_base_de_données>`

ajouter une collection 
`<nom_de_la_base_de_données>.<nom_de_la_collection>`

ajouter un ou plusieurs documents 

`db.<nom_de_la_collection>.insertOne({"field1": "value1", "field2": "value2"})`

`db.<nom_de_la_collection>.insertMany([{}, {}])`

insertMany prend une liste.

Mongodb génére un identifiant insertedId.

Retrouver les documents:

tous les documents:
`db.<nom_de_la_collection>.find()`

un seul:
`db.<nom_de_la_collection>.find({"filed": "value"})`

## Utiliser pymongo

[documentation officielle](https://pymongo.readthedocs.io/en/stable/index.html)


## Pour connecter Flask et MongoDB

[flask-pymongo](https://github.com/dcrosta/flask-pymongo/)