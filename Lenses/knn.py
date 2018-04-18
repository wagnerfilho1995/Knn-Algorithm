#-*- coding: utf-8 -*-

import math

#	Data
'''
	1. age of the patient: (1) young, (2) pre-presbyopic, (3) presbyopic
    2. spectacle prescription:  (1) myope, (2) hypermetrope
    3. astigmatic:     (1) no, (2) yes
    4. tear production rate:  (1) reduced, (2) normal
'''
D = [ 
	[1,  1,  1,  1,  1,  3],
	[2,  1,  1,  1,  2,  2],
	[3,  1,  1,  2,  1,  3],
	[4,  1,  1,  2,  2,  1],
	[5,  1,  2,  1,  1,  3],
	[6,  1,  2,  1,  2,  2],
	[7,  1,  2,  2,  1,  3],
	[8,  1,  2,  2,  2,  1],
	[9,  2,  1,  1,  1,  3],
	[10, 2,  1,  1,  2,  2],
	[11, 2,  1,  2,  1,  3],
	[12, 2,  1,  2,  2,  1],
	[13, 2,  2,  1,  1,  3],
	[14, 2,  2,  1,  2,  2],
	[15, 2,  2,  2,  1,  3],
	[16, 2,  2,  2,  2,  3],
	[17, 3,  1,  1,  1,  3],
	[18, 3,  1,  1,  2,  3],
	[19, 3,  1,  2,  1,  3],
	[20, 3,  1,  2,  2,  1],
	[21, 3,  2,  1,  1,  3],
	[22, 3,  2,  1,  2,  2],
	[23, 3,  2,  2,  1,  3],
	[24, 3,  2,  2,  2,  3]
	]

amostras = 24
classes = ["should be fitted with hard contact patients.",
 		   "should be fitted with soft contact patients.",
 		   "should not be fitted with contact patients."]


#	Retorne a Distancia entre dois elementos
def distance(x0, x, y0, y, z0, z, w0, w):
	return math.sqrt( pow(x-x0, 2) + pow(y-y0, 2) + pow(z-z0, 2) + pow(w-w0, 2) )

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
#	Main
patients = [0]*amostras
i = 0
#	Pegue os dados da tabela de entrada
while i < amostras:
	patients[i] = D[i]
	i += 1

w = -1
s = ""
while w != 0 or s != "0":

	#	Lista das classificações
	classificacao = []

	#	Contadores de quanto de cada tipo foram classificados
	t1 = t2 = t3 = 0

	print("\nClassifique!")
	print("1 - Individualmente")
	print("2 - Todos de uma vez")
	print("\n\n0- Sair")
	w = int(input())

	if w == 0: break
	elif w == 1:
		print("Escolha um paciente de 1 a 24 para classificar:")
		p = int ( input() )
		p += 1
		dist = []
		print("Defina um k: ")
		k = int ( input() )

		for i in range(0, amostras):
			
			if i != p:
				d = distance( 	patients[p][1], patients[i][1],
								patients[p][2], patients[i][2],
								patients[p][3], patients[i][3],
								patients[p][4], patients[i][4])
				dist.append([d, patients[i]])
		t = knn(dist, k)
		print("O paciente {} foi classificado como {} - (Classe {})".format(p-1, classes[t-1], t )) 

	elif w == 2:
		print("Defina um k: ")
		k = int ( input() )
		for i in range(0, amostras):

			dist = []

			for j in range(amostras):
				#	Se o paciente não for o proprio que estamos analisando, calcule a distancia entre ele e o outro
				if j != i:
					d = distance( patients[i][1], patients[j][1],
								  patients[i][2], patients[j][2],
								  patients[i][3], patients[j][3],
								  patients[i][4], patients[j][4])
					dist.append([d, patients[j]])
			t = knn(dist, k)
			classificacao.append( [patients[i][0], classes[t-1]] )
			if t == 1: t1 += 1
			elif (t) == 2: t2 += 1
			elif t == 3: t3 += 1

		for i in range(amostras):
			dupla = classificacao[i]
			#print("P{} -> {}".format(dupla[0], dupla[1]))
			
		print("\n==============================================\nResultados:")
		print("Classificados:{} pacientes -> {:.2f}% of the patients {} - (Classe {})".format( t1, (t1/amostras)*100, classes[0], 1))
		print("Classificados:{} pacientes -> {:.2f}% of the patients {} - (Classe {})".format( t2, (t2/amostras)*100, classes[1], 2))
		print("Classificados:{} pacientes -> {:.2f}% of the patients {} - (Classe {})".format( t3, (t3/amostras)*100, classes[2], 3))
		print("==================================================\n\n")
	print("\nDigite alguma tecla diferente de '0' para testar novamente")
	s = input()
print("Até Mais! e Que a força esteja com você!")