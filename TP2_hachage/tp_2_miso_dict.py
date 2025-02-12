import matplotlib.pyplot as plt
import numpy as np
import time
import sys



###### PARTIE 2 ######

def experiment_load_factor(load_factors):
	"""
	Étude du facteur de charge
	"""
	return [],[],[]

def experiment_longest():
	"""
	TODO: que fait cette fonction
	"""
	d = {}
	insertion_times = []

	for i in range(10000):
		key = str(i)
		value = i
		start_time = time.time()
		d[key] = value
		insertion_time = time.time() - start_time
		insertion_times.append(insertion_time)
	frequencies = np.histogram(insertion_times)[0]
	return frequencies

def visualisation(load_factors, insertion_times, num_resizes, sizes, frequencies):
	"""
	Visualisation des résultats
	"""
	# Temps d'insertion en fonction du facteur de charge

	# Nombre de réallocations de mémoire en fonction du facteur de charge
	
	# Taille de mémoire occupée en fonction du nombre d'éléments
	
	# Deuxième étude
	f = list()
	plt.figure(figsize=(10, 6))
	plt.bar(range(len(f)), f)
	plt.xlabel('Temps d\'insertion (s)')
	plt.ylabel('Fréquence')
	plt.title('Histogramme des fréquences des temps d\'insertions')
	plt.yscale('log')
	xticks = np.logspace(-6, 1, 3)  
	xtick_labels = [f'{x:.1e}' for x in xticks]  
	plt.xticks(xticks, xtick_labels)    
	plt.savefig('histogramme.png')

load_factors = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
insertion_times, num_resizes, sizes = experiment_load_factor(load_factors)
frequencies = experiment_longest()
visualisation(load_factors, insertion_times, num_resizes, sizes, frequencies)
