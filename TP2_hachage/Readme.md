# TP Hachage



 
# Partie 1 - Réaliser une fonction de hachage minimale parfaite 

On travaillera sur `tp_2_miso_mphf.py`.

Tout d'abord, voyons ensemble l'idée de la construction de la MPHF.
Puis suivez les commentaires dans le code à compléter.
Vous devez 
- finaliser la fonction pour construire la MPHF (`construction_mphf`), 
- écrire la fonction pour obtenir le hash d'un élément par la MPHF (`get_hash_mphf`), 
- écrire la fonction pour créer une table de hachage avec cette mphf (`create_hash_table`)

Ecrivez vos réponses et commentaires dans ce document.

Puis décommenter `compare_taille` à la fin et expliquer les résultats.

Bonus : faites varier `nb_niveaux` et `gamma`, voyez quelle influence ils peuvent avoir.

# Partie 2 - Analyse de performance de dictionnaires en Python

On travaillera sur `tp_2_miso_dict.py`

A la fin de cette partie, en lançant `python tp_2_miso_dict.py` on doit obtenir 4 graphiques.

## Introduction

Nous allons analyser la performance de dictionnaires `dict` en Python en fonction de différents facteurs : que le facteur de charge (loading factor), 
le temps d'insertion et la taille de la mémoire occupée. Vous pourrez utiliser matplotlib et numpy pour visualiser les résultats.

##  Étude du facteur de charge

Fonction `experiment_load_factor`:

0. La fonction `experiment_load_factor` doit être définie pour prendre en entrée une liste de facteurs de charge (`load_factors`) et renvoyer les temps 
- d'insertion de clefs, 
- les nombres de réallocations de mémoire (quand le dictionnaire est ré-écrit en mémoire pour agrandir sa taille) 
- et les tailles de mémoire occupées par le dictionnaire pour chaque facteur de charge. 

1. Initialisation des listes pour stocker les résultats.
Initialiser dans la fonction `experiment_load_factor` des listes `insertion_times`, `num_resizes` et `sizes` seront utilisées pour stocker les trois résultats décrits au dessus.

2. La fonction `experiment_load_factor` doit boucler sur chaque facteur de charge de la liste en entrée `load_factors`. Créer un dictionnaire d'abord vide à chaque fois.

3. Initialiser les variables `num_elements`, `start_time`, `num_resize` et `last_size` pour respectivement mesurer  le nombre d'éléments, le temps d'insertion et le nombre de réallocations de mémoire.

4. Insérer les éléments dans le dictionnaire et mesurer le temps d'insertion pour chaque élément, vérifier le nombre de réallocations mémoire (utiliser par exemple `time.time()` et `sys.getsizeof()` pour mesurer le temps et la taille du dictionnaire avant et après chaque insertion).

5. Pour un facteur de charge donné, stocker les résultats dans les listes `insertion_times`, `num_resizes` et `sizes`.

## Deuxième étude

6. A quoi sert la fonction `experiment_longest` ?

## Visualisation des résultats

7. Créez quatre graphiques au format png ou pdf : 

- Un graphique du temps d'insertion en fonction du facteur de charge (obtenu question 5)
- Un graphique du nombre de réallocations de mémoire en fonction du facteur de charge (obtenu question 5)
- Un graphique de la taille de mémoire occupée en fonction du nombre d'éléments (obtenu question 5)
- Un histogramme des fréquences des temps d'insertions discrétisés (code fourni, remplacer la liste vide par la bonne entrée)

10. Commentez vos résultats.
