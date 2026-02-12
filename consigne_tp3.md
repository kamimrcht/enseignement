# Dernier TP de SD :( 2026

Durant cette UE avons :

- codé comme un.e programmeur ou programmeuse de structures de données
- fait de la biblio, présenté des méthodes et résultats comme un chercheur ou une chercheuses
- nous allons maintenant répondre à un cahier des charges comme un.e... bioinformaticien.ne, sur un problème qui est une question ouverte en bioinformatique : **comment effectuer le plus rapidement une intersection entre ensembles de k-mers**


# Projet:  intersection rapide d’ensembles de k-mers

## Objectif

L’objectif de ce projet est de concevoir, implémenter et évaluer **une ou plusieurs méthodes permettant de calculer efficacement l’intersection de deux ensembles de k-mers**.

Le programme devra produire :

1. **Le nombre de k-mers appartenant à l’intersection**
2. **Un fichier FASTA contenant les k-mers de l’intersection**

Vous devrez mesurer :

* Temps d’exécution (notre principal intérêt)
* Mémoire consommée 

Les tests devront être réalisés sur **plusieurs tailles d’ensembles** (à générer avec des `head` successifs)

On pourra donc afficher un tableau  ou un graphique avec les vitesses d'exécution en ordonnée et les tailles (10.000 reads, 100.000 reads, ...) en abscisse, même chose pour la mémoire. Vous pourez utiliser `/usr/bin/time` pour la mesure du temps et de la RAM sous linux.


## Données 

Vous disposerez de **deux jeux de données de séquençage**.

A télécharger comme suit : 

` wget https://s3.amazonaws.com/logan-pub/u/SRR8615240/SRR8615240.unitigs.fa.zst `

` wget https://s3.amazonaws.com/logan-pub/u/SRR8615242/SRR8615242.unitigs.fa.zst `



Vous trouverez aussi le résultat prévu : un fichier contenant la liste de k-mers qui est effectivement dans l'intersection (k = 25), pour vérifier vos résultats, ici : 

`https://filesender.renater.fr/?s=download&token=7a3c063f-1b59-4223-9c84-b62b032d9ce3`

**Conseil:** pour tester et prototyper, utiliser une fraction des jeux de données avec un `head`

## Méthodes autorisées

Toutes ! Vous pouvez :

- Utiliser une librairie existante, un outil bioinformatique externe, des structures Python ou d'un autre langage (tables de hachage, etc)
- Implémenter votre propre solution
- Combiner plusieurs approches

La démarche est de tester des approches.


## Évaluation

- Description/justification des méthodes/structures de données choisies (originalité par rapport aux autres groupes, si pertinente)
- Graphique ou tableau avec les performances pour au moins une méthode, axes ou colonnes bien nommés
- Questions à chaque groupe pendant le développement
- Remarque sur les performances, les compromis (temps versus mémoire, faux positifs, ...)
- Le tout dans un PDF rapport, nous fixons une date de rendu
- Bonus : aller plus vite que la solution de la prof
