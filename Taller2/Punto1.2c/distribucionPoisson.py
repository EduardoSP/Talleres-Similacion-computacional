#=====Punto 1.2 c) Generacion de datos distribucion poisson con parametro lambda=3.5 ==========
#Nota: Estoy siguiendo la logica del algoritmo de la diapositiva del curso numero 99
from GEM import Generate_values_r
import math

r = []

#function for to calculate the algorithm of poisson
def Exec_dist_Poisson(random, lambda_value):
	A = math.exp(-lambda_value)
	n = 0
	R = 1
	while R >= A:
		R = R * random
		n += 1
	n = n - 1 
	return n

#executing main 
if (__name__=="__main__"):
	rows_calc = 100000 #Quantity of data for to generate
	lambda_value = 3.5 # value of lambda
	r = Generate_values_r(rows_calc) # value of r. receives the amount of data to generate
	for i in range(len(r)): # calculate para each value of r
		print str(Exec_dist_Poisson(r[i], lambda_value))#calling function for to calculate the algorithm of poisson