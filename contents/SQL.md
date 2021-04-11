---
title: SQL révisions
status: publish
date: 20-03-2021
---
## les commandes SQL de base

### tutoriels

[le tutoriel de postgreSQL](https://www.postgresqltutorial.com/) Toutes les commandes expliquées.

[le tutoriel de w3schools](https://www.w3schools.com/sql/default.asp) idem avec des exercices.

### pour manipuler des données

	INSERT INTO table_name(column1, column2, …)
	VALUES (value1, value2, …);

	UPDATE table_name
	SET column1 = value1,
    	    column2 = value2,
    	    ...
	WHERE condition;

	DELETE FROM table_name
	WHERE condition;

### Sélectionner des données

	SELECT
   	    select_list
	FROM
   	    table_name;

### Gérer les tables
	
	CREATE TABLE [IF NOT EXISTS] table_name (
   		column1 datatype(length) column_contraint,
   		column2 datatype(length) column_contraint,
   		column3 datatype(length) column_contraint,
   		table_constraints
	);

	ALTER TABLE table_name 
	RENAME TO new_table_name;

	ALTER TABLE table_name 
	ADD COLUMN column_name datatype column_constraint;

	ALTER TABLE table_name 
	DROP COLUMN column_name;

	ALTER TABLE table_name 
	RENAME COLUMN column_name 
	TO new_column_name;

voir les tutoriels.
	
### cours sur les bases de données relationnelles

[cours d'Udacity](https://www.udacity.com/course/intro-to-relational-databases--ud197) Connaissances de bases requises en Python. Durée de 4 semaines. Gratuit.

### bac à sable pour s'entraîner

[sql fiddle](http://sqlfiddle.com/) voir la partie 'View Execution Plan' pour trouver les zones d'amélioration d'une requête.

### pour aller plus loin

[use the index, luke](https://use-the-index-luke.com/) site pour apprendre à optimiser les requêtes SQL. Voir aussi l'utilisation des index sur le tutoriel postgreSQL.
