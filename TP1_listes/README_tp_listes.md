# TP 1 : listes

Pré-requis : cours d'intro aux structures de données et listes
intro à Github: avoir un compte.


Dans ce TP on va commencer par implémenter une liste chaînée (LinkedList) avec quelques opérations basiques.
Sur mon github, dans le répertoire enseignement, vous allez trouver un dossier TP1_listes
Clonez-le.

Joignez ce fichier README à votre dépôt sur Github, puisque certaines réponses sont à rédiger dedans.
Ajoutez aussi le code.


NOTA BENE : il est INTERDIT d'utiliser les `set` ou les `dict` dans ce TP parce qu'on les verra plus tard :-)


# Evaluation:
Les TP sont évalués par groupes de 2, éventuellement 3.

partie écrite du TP : 
- chaque groupe a un répertoire Github avec un nom explicite comme "TP1_SD"
- ce fichier `README_tp_listes.md` et le fichier Python `linkedList.py` sont dans le répertoire
- vous avez répondu aux questions dans `README_tp_listes.md`
- chaque membre du groupe a fait plusieurs commits dans le code
- il y a des tests où cela est requis
- quand j'exécute `python linkedList.py` avec votre code, aucune erreur ne s'affiche
- le code est commenté si nécessaire
- le code est correct
- quand j'exécute votre code, un graphique en .png ou .pdf est généré
- ce graphique est correct
- vos réponses aux questions sont correctes
- on décide d'une date de rendu ensemble : je ne prends pas en compte les commits postérieurs à la date de rendu

partie orale du TP :
- je vous interroge sur certaines de vos réponses aux questions

# Questions

0. Regardez le fichier linkedList.py, il est composé de code à trou qu'il faudra remplir pour répondre à ce TP.

Voyez d'abord la classe Node : elle représente un noeud dans une liste chaînée.
Chaque noeud contient des données (`self.data`) et une référence au noeud suivant (`self.next`).

Voyez ensuite la classe LinkedList: elle représente une liste chaînée.
Regardez dans les commentaires, certaines lignes commencent par `>>>` suivis de code Python directement intégrés dans les commentaires. 
Ce sont des doctests! Python sait les interpréter et va les exécuter. Il attend:
`>>> resulat = ligne de code`
`resultat_attendu`
et va vérifier que `resultat == resultat_attendu`
Si les doctests fonctionnenent, vous n'aurez aucun message particulier dans la console en lançant `python linkedList.py`, dans le cas contraire, vous verrez s'afficher des messages d'erreur.

J'ai mis beaucoup de tests pour la classe, et beaucoup ne s'effectueront pas correctement avant que vous ayez avancé dans le tp. C'est normal !

`def __init__(self):` initialise la liste, d'abord vide.

Si vous tentez de lancer `python linkedList.py` dans votre terminal, vous devriez avoir beaucoup d'erreurs dues aux tests.

1. Maintenant c'est à vous, implémentez une méthode `append(self,data)` qui ajoute un élément à la liste.
(pour cette première méthode, je vous ai également rédigé des doctests)


2. Rédigez une méthode `get(self,index)` qui récupère la valeur à un index donné (l'équivalent pour une liste Python serait `[]`).

3. Pour cette méthode (*ce sera vrai aussi pour les suivantes*), rédigez des doctests. A quels cas doit-on penser ?


4. Rédigez une méthode `delete(self, index)` qui supprime un élément à un index donné dans la liste + doctests

5. Petit point sur la méthode `__iter__(self)` que j'ai implémentée pour vous.
Déjà que signifie `__` ? Cela signifie qu'on a affaire à une **méthode spéciale** que Python connait déjà, mais qu'on ré-implémente ici pour le cas spécifique de notre `LinkedList`: on est en train de personnaliser les fonctions de Python pour notre objet!

Ensuite qu'est ce que `iter` ? C'est un itérateur. Sans rentrer dans les détails, cela permet d'itérer sur des objets comme des listes. Les itérateurs sont faits pour aller vite quand on itère, et sont appelés implicitement quand on appelle `for` par exemple, sur un itérable (exemples d'itérables : une `List()`, on itère sur ses éléments, une `String`, on itère sur ses caractères, ...)

Pour mettre en pratique le fait de surcharger, surchargez la méthode spéciale `__len__(self)` pour nos listes. (+doctest)

6. Nous avons déjà bien avancé. Voyez plus bas dans le fichier un `main` dans lequel appeler des fonctions.
J'ai ajouté deux fonctions : une qui génère une séquence de nucléotides aléatoire, une qui extrat des k-mers d'une séquence donnée dans une liste Python nommée `kmers`. 

Faites grossir la séquence initiale à 10000 bases.

Avec `import time` et `time.perf_counter()`, mesurez et écrivez le temps nécessaire à mettre les k-mers de `sequence` dans `kmers`

7. Ajouter un code similaire pour mettre les k-mers de la séquence dans votre `LinkedList`, reportez également le temps.

8. Ecrivez une fonction `def contient_linked(L:LinkedList,e:string):` à laquelle on passe une liste chainée et un élement, et qui vérifie si l'élément est dans la liste. Parcourez chaque élément en vous aidant de la structure de la liste chaînée : la boucle for est interdite !

8. Ecrivez une fonction `def contient(L,e):` à laquelle on passe un objet L comme une List ou une linked list + un élément e, et qui vérifie si e est dans L.

9. Finalement, à quoi nous a servi de surcharger `__iter__(self)` ?

10. Passez la liste Python avec les k-mers, ainsi que le k-mer `lookup` à `contient`, mesurez le temps.

11. Faites de même pour la `LinkedList` pour les fonctions `contient` et `contient_linked`

12. Decommentez la fonction `boucle_naive`, que fait-elle ? Passez lui, comme au dessus, `kmers` et votre `LinkedList`, mesurez les temps de la même manière.

13. Finalement, à quoi nous a servi de surcharger `__len__(self)` ? 

14. Que remarquez vous avec cette dernière fonction ? Faites un petit travail de recherche pour m'expliquer simplement pourquoi.

15. Faites varier la taille de séquences pour avoir au moins 4 ou 5 listes de k-mers de tailles différentes. Collectez les temps pour les trois fonctions qui recherchent des k-mers dans les listes (`contient`, `contient_linked` et `boucle_naive`), et pour les deux types de listes. Ecrivez une fonction qui prend en entrée ces temps, et affiche, pour chaque combinaison possible liste x fonction, les temps d'exécution pour des nombre de k-mers croissants.

Note : en exécutant votre code, je dois pouvoir produire ce graphique en .png ou .pdf

16. Vis à vis de ce que nous avons vu en cours, quels sont vos commentaires sur cette figure ?

17. Pourquoi ai-je designé une expérience avec un k-mer `lookup` arbitraire à chercher dans une séquence générée aléatoirement ? 

18. Bonus : si nous testions un `array` à la place d'une `List` ? Comment s'y prendre ? Est-ce que ça améliore la recherche, et pourquoi ? 

19. Bonus 2 : dé-commentez le code #bonus2. C'est aussi une recherche du k-mer. Bonus pour le/la première étudiant.e qui a fini son TP et vient m'expliquer ce qu'il se passe sur le temps d'exécution.


