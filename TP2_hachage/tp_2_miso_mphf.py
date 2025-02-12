import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import random


###### PARTIE 1 ######

def construction_mphf(set_kmer, n, gamma=2, nb_niveaux=3):
	
	"""
	Construit une fonction de hachage minimale parfaite (MPHF) pour un ensemble de k-mers.

	Parameters:
	set_kmer (set): Ensemble de k-mers.
	n (int): Taille de l'ensemble de k-mers.
	gamma (int): Facteur de réduction de la taille de la table de hachage. Default: 2.
	nb_niveaux (int): Nombre de niveaux de réduction de la taille de la table de hachage. Default: 3.

	Returns:
	mphf (list): Table de hachage minimale parfaite.

	Examples:
	>>> set_kmer = {str(i) for i in range(10)}
	>>> n = 10
	>>> mphf = construction_mphf(set_kmer, n)
	>>> len(mphf) == n
	True
	>>> all(0 <= mphf[i] < n for i in range(n))
	True
	>>> len(mphf) == n
	True
	"""
	# Initialisation
	set_kmer_courant = set_kmer.copy()
	tableaux = []
	collision = set()
	for _ in range(nb_niveaux):
		if len(set_kmer_courant) > 0:
			l = len(set_kmer_courant)
			tableau_principal = [-1] * (gamma * l)
			for kmer in set_kmer_courant:
				pass # compléter
				# hacher le k-mer (attention, hash() peut rendre des entiers signés, nous voulons des entiers positifs)
				# récupérer l'adresse
				# si le tableau principal est déjà rempli à l'adresse:
					# mettre le kmer dans collision()
					#sinon, écrire le hash à l'adresse dans le tableau principal

			tableaux.append(tableau_principal) # expliquer
			set_kmer_courant = collision.copy() # expliquer
			collision = set() # expliquer

	# Construction de la MPHF
	mphf = [] 
	grand_tableau = []
	for tableau in tableaux:
		grand_tableau.extend(tableau) # expliquer

	rangs = []
	max_rang = 0
	i = 0
	for kmer in set_kmer:
		pass # compléter:
		# hacher le kmer
		# si le hash est dans le grand_tableau
			# récupérer son index
			# récupérer son rang (utiliser la fonction count())
			# ajouter à la mphf [h, rang]
			# mettre à jour max_rang

	for kmer in set_kmer_courant: #gestion des collisions: expliquer les 3 lignes du dessous
		max_rang += 1
		h = abs(hash(kmer))
		mphf.append([h, max_rang])
	
	return mphf


def get_hash_mphf(mphf, kmer):
	"""
	Calcule le hash d'un k-mer à l'aide d'une fonction de hachage minimale parfaite (MPHF).

	Parameters:
	mphf (list): Table de hachage minimale parfaite.
	kmer (str): K-mer à hasher.

	Returns:
	int: Hash du k-mer.

	Examples:
	>>> set_kmer = {str(i) for i in range(10)}
	>>> n = 10
	>>> mphf = construction_mphf(set_kmer, n)
	>>> kmer = "5"
	>>> hash_mphf = get_hash_mphf(mphf, kmer)
	>>> 0 <= hash_mphf < n
	True
	"""
	pass # TODO modifier

def create_hash_table(set_kmer, n):
    """
    Crée une table de hachage à partir d'un ensemble de k-mers et d'une mphf

    Parameters:
    set_kmer (set): Ensemble de k-mers.
    n (int): Taille de la table de hachage.

    Returns:
    list: Table de hachage créée à partir des k-mers
    mphf: la mphf

    Examples:
    >>> set_kmer = {'ATCG', 'TGCA', 'GCTA'}
    >>> n = 10
    >>> tableau = create_hash_table(set_kmer, n)
    >>> len(tableau) == n
    True
    >>> all(kmer in tableau for kmer in set_kmer)
    True
    """
    pass # TODO modifier
    # créer la mphf pour les kmers
    # initialiser un tableau de taille n (une liste)
    # écrire les kmers aux adresses du tableau données par la mphf
    # retourner le tableau et la mphf




def generer_kmers(n, k):
	'''
	genere un set de n k-mers
	'''
	kmers = set()
	while len(kmers) < n:
		kmer = ''.join(random.choice('ATCG') for _ in range(k))
		kmers.add(kmer)
	return kmers


def compare_taille(n_max, fichier_sortie):
	n_values = []
	table_size = []
	dict_size = []
	encoding_size = []
	k = 21
	
	for n in range(100, n_max, 1000):
		set_kmer = generer_kmers(n, k)
		tableau, mphf = create_hash_table(set_kmer,n)

		n_values.append(n)
		table_size.append(sys.getsizeof(tableau)+sys.getsizeof(mphf)) # pourquoi ici on ne mesure pas juste la taille en mémoire du tableau ? 
		dict_size.append(sys.getsizeof(set_kmer))
		encoding_size.append(n * 2 * k / 8)  # expliquer ce que c'est

	plt.plot(n_values, table_size, label='Table avec MPHF')
	plt.plot(n_values, dict_size, label='Dict')
	plt.plot(n_values, encoding_size, label='Adressage direct des clés')
	plt.xlabel('n')
	plt.xticks(n_values, [str(x) for x in n_values], rotation=45)
	plt.ylabel('Taille (octets)')
	plt.title('Évolution de la taille de la table de hachage avec MPHF, du dict et de l\'adressage direct des clés')
	plt.legend()
	plt.savefig(fichier_sortie)
	plt.close()

# dé-commenter quand vous êtes prêts, expliquer les résultats
#compare_taille(10000,"mphf.png")
