import random

#function for generate the numbers pseudorandoms of three decimals
#Return one list with the pseudoaleatorios according to amount of pseudorandom 
#Nota esta generando el numero 1 por el redondeo
def Pseudo_random(amount_pseudoRandom,amount_decimal):
	list_pseudoRandom=[]
	for i in range(amount_pseudoRandom): #while according the numbers pseudo random
		random_number = round(random.random(),amount_decimal)# generation of numbers pseudoaleatorios with three decimals
		list_pseudoRandom.append(random_number)
	return list_pseudoRandom
