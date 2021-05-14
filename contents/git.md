---
title: Utiliser Git
draft: False
date: 03-03-2021
---
## Tutoriel

[tutoriel](https://realpython.com/python-git-github-intro/) excellent site pour apprendre

## Utiliser les branches

Pour travailler en équipe, sans impacter la version principale sur main / master.

Se déplacer ou créer une nouvelle branche (pas d'espace dans le nom)

`git checkout -b 'nom-de-la-branche'`

Procédure d'enregistrement sur la branche

`gst`

`git add .`

`git commit -m'nom-qui-a-du-sens'`

`git push origin nom-de-la-branche`

Pour intégrer la branche sur la version principale (pull request)

sur github, pull request

click pull merge

Pour remettre la version principale sur son poste

`git checkout master` raccourci `gco`

`git pull origin master`

Pour nettoyer les branches qui ont été intégrées

`git sweep`

Montrer les branches

`git branch`

Remettre la version principale sur la branche

`git merge master` 


montre les branches

`git branch`
