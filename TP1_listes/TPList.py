"""
Ce code implémente une liste chaînée simple avec les opérations : 
- ajouter un élément à la fin de la liste (append)
- récupérer un élément par son index (get)
- supprimer un élément par son index (delete)

chaque méthode est testée à l'aide de doctests 
"""
from array import array
from typing import Iterable
from random import choice
import string
import time


class TPList:
	"""
	Classe pour représenter une liste chaînée.

	>>> ll = TPList()
	>>> ll.append(10)
	>>> ll.append(20)
	>>> ll.append(30)
	>>> ll.get(0)
	10
	>>> ll.get(1)
	20
	>>> ll.get(2)
	30
	>>> ll.get(3) is None
	True
	>>> len(ll)
	3
	>>> ll.delete(1)
	>>> len(ll)
	2
	>>> ll.delete(0)
	>>> len(ll)
	1
	>>> ll.delete(0)
	>>> len(ll)
	0
	>>> for value in ll:  # Test de l'itération
	...     print(value)
	"""
	def __init__(self):
		"""
		Initialise une liste chaînée vide avec une tête nulle.
		"""
		self.head = None
		self._size = 0  # Stocke la taille de la liste

	def append(self, data):
		"""
		Ajoute un élément à la fin de la liste.
		
		:param data: La valeur à ajouter à la liste.
		
		>>> ll = TPList()
		>>> ll.append(10)
		>>> ll.get(0)
		10
		>>> ll.append(20)
		>>> ll.get(1)
		20
		"""
		pass

	def get(self, index):
		"""
		Récupère la valeur à un index donné dans la liste.
		
		:param index: L'index de l'élément à récupérer (0-based).
		:return: La valeur de l'élément ou None si l'index est invalide.
		"""
		pass

	def delete(self, index):
		"""
		Supprime un élément à un index donné dans la liste.
		
		:param index: L'index de l'élément à supprimer (0-based).
		"""
		pass

	def __iter__(self):
		"""
		Permet d'itérer sur la liste chaînée.
		
		>>> ll = TPList()
		>>> ll.append(10)
		>>> ll.append(20)
		>>> ll.append(30)
		>>> [value for value in ll]
		[10, 20, 30]
		"""
		current = self.head
		while current:
			yield current.data
			current = current.next

	def __len__(self): 
		"""
		Retourne la longueur de la liste chaînée.
		"""
		pass

class Node:
	"""
	Classe pour représenter un noeud dans une liste chaînée.
	Chaque noeud contient des données et une référence au noeud suivant.
	"""
	def __init__(self, data):
		self.data = data
		self.next = None



if __name__ == "__main__":
	import doctest
	doctest.testmod()


	def generate_sequence(length=1000):
		"""Génère une séquence aléatoire de bases de longueur donnée."""
		return ''.join(choice('ACGT') for _ in range(length))

	def extract_kmers(sequence, k=31):
		"""Extrait tous les k-mers d'une séquence donnée."""
		return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

	lookup = "CTCATAATTAGGGAGATTTATGCGTGGGGGC" #kmer à chercher
	
	# Créer la séquence et extraire les k-mers
	sequence = generate_sequence(50000)
	kmers = extract_kmers(sequence, 31)


	


	def contient_TP(L:TPList,e:string):
		"""
		:param L: une TP list
		:param e: un élément à chercher dans la liste
		"""
		pass
			
	def contient(L,e):
		"""
		:param L: un iterable comme une liste
		:param e: un élément à chercher dans la liste
		"""
		for kmer in L:
			pass
	
	#def boucle_naive(L,e):
	#	for i in range(len(L)):
	#		if L.get(i) == e:
	#			return True
	#	return False
	
	
	
	# bonus
	#try:
	#	sequence.index(lookup)
	#except:
	#	None
	
	
	
