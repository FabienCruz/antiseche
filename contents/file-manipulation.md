---
title: Manipuler des fichiers et des répertoires
draft: False
date: 12-12-2020
---
## Tutoriels

- [Tutoriel sur pathlib](https://realpython.com/python-pathlib/) Utilisation de pathlib.

- [Aide-mémoire sur pathlib](https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf) en une page les principales méthodes de pathlib. Synthétique et visuel.

- [Tutoriel](https://realpython.com/working-with-files-in-python/) avec les principales actions de manipulation de fichier et de répertoire, plus classique avec les chaînes de caractères.


## Bibliothèques utiles

- [pathlib](https://docs.python.org/fr/3/library/pathlib.html)pathlib est une bibliothèque existante depuis python3.4 qui permet d'utiliser des objets pour les chemins de répertoire, plutôt que leur représentation sous forme de chaîne de caractère. La différence est expliquée sur ce [blog](https://snarky.ca/why-pathlib-path-doesn-t-inherit-from-str/). **Pathlib permet de naviguer entre les dossiers et de gérer les fichiers, en très peu de lignes de code.**

- [os](https://docs.python.org/fr/3/library/os.html) Utilitaires sur le système d'exploitation (os). Afficher le chemin, ouvrir un fichier ...

- [glob](https://docs.python.org/fr/3/library/glob.html?highlight=glob#module-glob)Recherche et navigation entre les répertoires.Par exemple, lister tous les fichiers '.csv' d'un sous-répertoire. 

- [shutil](https://docs.python.org/fr/3/library/shutil.html#module-shutil)pour les opérations sur les fichiers et les ensembles de fichiers. Les chemins sont des chaînes de caractères. Certaines 'metadatas' (la dated' enregistrement du fichier par exemple) peuvent être perdues.
