#-*- coding: utf-8 -*-

import math

#	Summary Statistics
#				Min  Max   Mean    SD   Class Correlation
sepal_length = [4.3, 7.9,  5.84,  0.84,   0.7826]
sepal_width =  [2.0, 4.4,  3.05,  0.43,  -0.4194]
petal_length = [1.0, 6.9,  3.76,  1.76,   0.9490]
petal_width =  [0.1, 2.5,  1.20,  0.76,   0.95650]	

amostras = 150
classes = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]

'''
#	Normalização do Valor
def normal(v, atr):
	if atr == 1:
		numerador = v - sepal_length[0]
		denominador = sepal_length[1] - sepal_length[0]
	elif atr == 2:
		numerador = v - sepal_width[0]
		denominador = sepal_width[1] - sepal_width[0]
	elif atr == 3: 
		numerador = v - petal_length[0]
		denominador = petal_length[1] - petal_length[0]
	elif atr == 4: 
		numerador = v - petal_width[0]
		denominador = petal_width[1] - petal_width[0]

	return numerador/denominador
'''
#	Retorne a Distancia entre dois elementos
def distance(x0, x, y0, y, z0, z, w0, w):
	return math.sqrt( pow(x-x0, 2) + pow(y-y0, 2) + pow(z-z0, 2) + pow(w-w0, 2))

def knn ( dist, k ):
	dist.sort()
	c = [[0, 1],
		 [0, 2],
		 [0, 3]]
	i = 0
	while i < k:
		dupla = dist[i]
		if dupla[1][5] == 1:
			c[0][0] += 1
		elif dupla[1][5] == 2:
			c[1][0] += 1 
		elif dupla[1][5] == 3:
			c[2][0] += 1 
		i += 1
	
	c.sort(reverse = True)
	return c[0][1]

def readFiles( name_m1 ):

	matrix1 = []
	iris = []

	readM1 = open(name_m1, 'r')

	for i in range(0, amostras):
		matrix1 += 	[list(map( str, readM1.readline().split(',') ))]
		
		five = matrix1[i]
		doub1 = float(five[0])
		doub2 = float(five[1])
		doub3 = float(five[2])
		doub4 = float(five[3])
		s = five[4].replace('\n', '')
		if s == "Iris-setosa": tipo = 1
		elif s == "Iris-versicolor": tipo = 2
		elif s == "Iris-virginica": tipo = 3
		iris.append([i+1, doub1, doub2, doub3, doub4, tipo])
	
	readM1.close()

	return iris


#	Main

D = readFiles( 'iris.in')

w = -1
s = ""
while w != 0 or s != "0\n":

	classificacao = []
	t1 = t2 = t3 = 0

	print("\nClassifique!")
	print("1 - Individualmente")
	print("2 - Todos de uma vez")
	print("\n\n0- Sair")
	w = int(input())

	if w == 0: break
	elif w == 1:
		print("Escolha uma planta de 1 a 150 para classificar:")
		
		p = int ( input() )
		p -= 1
		dist = []
		
		print("Defina um k: ")
		k = int ( input() )

		for i in range(0, amostras):
			if i != p:
				d = distance( 	D[p][1], D[i][1],
								D[p][2], D[i][2],
								D[p][3], D[i][3],
								D[p][4], D[i][4])
				dist.append([d, D[i]])
		t = knn(dist, k)
		print("A planta {} foi classificada como {} - (Classe {})".format(p+1, classes[t-1], t )) 

	elif w == 2:
		print("Defina um k: ")
		k = int ( input() )
		for i in range(0, amostras):
			
			dist = []

			for j in range(amostras):
				if j != i:
					d = distance( D[i][1], D[j][1],
								  D[i][2], D[j][2],
								  D[i][3], D[j][3],
								  D[i][4], D[j][4])
					dist.append([d, D[j]])
			if i == 0:
				for i in range(20):
					print(dist[i])
			t = knn(dist, k)
			classificacao.append( [D[i][0], classes[t-1]] )

			if t == 1: t1 += 1
			elif (t) == 2: t2 += 1
			elif t == 3: t3 += 1

		for i in range(amostras):
			print(classificacao[i])	
		print("\n==============================================\nResultados:")
		print("Classificados:{} plantas -> {:.2f}%  {} - (Classe {})".format( t1, (t1/amostras)*100, classes[0], 1))
		print("Classificados:{} plantas -> {:.2f}%  {} - (Classe {})".format( t2, (t2/amostras)*100, classes[1], 2))
		print("Classificados:{} plantas -> {:.2f}%  {} - (Classe {})".format( t3, (t3/amostras)*100, classes[2], 3))
		print("==================================================\n\n")
	print("\nPressione alguma tecla para continuar")
	s = input()
print("Até Mais! Vida longa e Próspera!")
