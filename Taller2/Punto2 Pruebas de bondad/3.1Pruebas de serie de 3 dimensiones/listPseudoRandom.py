import random

#function for generate the numbers pseudorandoms of three decimals
#Return one list with the pseudoaleatorios according to amount of pseudorandom 
def Pseudo_random(amount_pseudoRandom,amount_decimal):
	list_pseudoRandom=[]
	for i in range(amount_pseudoRandom): #while according the numbers pseudo random
		#Nota cuando genero valores de 0 a 1 me salen numeros como 6.76 
		random_number = random.uniform(0.01, 0.9) # generation of numbers pseudoaleatorios 
		#random_number = random.uniform(0, 1.0) # generation of numbers pseudoaleatorio	
		random_number = str(random_number)
		random_number_3decimals =random_number[:random_number.find(".") + amount_decimal + 1] # pseudo random with three decimals
		list_pseudoRandom.append(float(random_number_3decimals) )
	return list_pseudoRandom
