#============================Punto 1 GEM(Generador estandar minimo)========================================

#Estandar minimo visto en clase Propuesto por Park y Miller(1988)
import random
from writeFile import Write_text_file
from arrayCreation import Create_array
#matriz= [] #array declaration global
#specific parameters
#===================================

a = pow(7,5) #multiplicate
c = 0 #increment
m=  pow(2,31) - 1 #mod

"""
#var prueba
a = 5 #multiplicate
c = 13 #increment
m=  7#mod
#==================
"""
#==================================
#Note: use the seed except the number zero
#seed generator
"""
X0=random.randint(1, 1000000)# seed of range 1 and 4999
"""

X0=27#var fixed seed


#values_r=[] #List for the values of r
#function to process the calculation of GEM
def Exec_generates_numbers(generates_numbers, values_r, matriz):
	n=0 #Especific the amount data
	Xn=X0 #assignment the value of seed 
	# while that runs the rows
	while(n < generates_numbers):
		matriz[n][0] = n
		matriz[n][1]= float(Xn)
		matriz[n][2] = float(((a * Xn) + c)%m) 
		matriz[n][3] = float((matriz[n][2])/m)
		Xn = float(matriz[n][2]) 
		values_r.append(matriz[n][3])
		n = n + 1;

##function for generate the values of r
#Receives the amount of numbers generated r
def Generate_values_r(generates_numbers):
	matriz= [] 
	matriz = Create_array(generates_numbers,4) #calling the function for the array creation depending rows and columns
	#Execute procces
	values_r=[]
	Exec_generates_numbers(generates_numbers, values_r, matriz)
	#print(matriz)
	return values_r
