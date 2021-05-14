---
title: Utiliser postgreSQL
draft: False
date: 21-03-2021
---
## Installation

PostgreSQL est installé par défaut sur les mac.

pour les autres systèmes d'exploitation [voir ici](https://www.postgresql.org/download/)

## Lignes de commande

pour se connecter avec un nom d'utilisateur et les droits associés

    sudo -u <username> -i

### création / suppression d'une base de données

pour créer une nouvelle base de données

    createdb <database_name>

pour supprimer une base de données

    dropdb <database_name>

pour mettre à zéro (suppimer puis créer)

    dropdb <database_name> && createdb <database_name>

### utilisation de psql

psql est une application terminal où il est possible de coder directement en SQL avec le terminal.

pour connecter psql et une base de données, avec un utilisateur particulier (optionnel)

    psql <database_name> [<username>]

exemple : psql ma_base nom_utilisateur

pour quitter psql

    \q

rappel: backslash ´alt + maj + /´

la liste des commandes est accessible via:

    \?

la liste des bases de données sur le serveur

    \l

se connecter à une (autre) base de données

    \c <dbname>

liste les tables de la base de données

    \dt

description d'une table

    \d <tablename>

## version application avec interface graphique

[Postgres.app](https://postgresapp.com/) une version application de Postgres, avec la possibilité d'interfaces graphiques.

[pgAdmin](https://www.pgadmin.org/) l'interface la plus populaire pour postgreSQL

[PopSQL](https://popsql.com/) utilisable avec postgreSQL mais aussi d'autres base de données
