#============================Punto 1 GEM(Generador estandar minimo)========================================

#Estandar minimo visto en clase Propuesto por Park y Miller(1988)
import random
from arrayCreation import Create_array
from WriteExcel import write_text_excel
from WriteExcel import write_text_excel_openpyxl
matriz= [] #array declaration global
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
X0=27#var prueba

#function to process the calculation of GEM
def Exec_generates_numbers(generates_numbers):
	n=0 #Especific the amount data
	Xn=X0 #assignment the value of seed 
	# while that runs the rows
	while(n < generates_numbers):
		matriz[n][0] = n
		matriz[n][1]= float(Xn)
		matriz[n][2] = float(((a * Xn) + c)%m) 
		matriz[n][3] = float((matriz[n][2])/m)
		Xn = float(matriz[n][2]) 
		#write line by line File
		#text_line = str(matriz[n][0]) +' --- '+ str(matriz[n][0]) + ' --- '+ str(matriz[n][1]) + ' --- '+ str(matriz[n][2]) + ' --- '+  str(matriz[n][3]) 
		#Write_text_file('Gem.txt', text_line, 'a') 	  
		n = n + 1;

#executing main 
if (__name__=="__main__"):
	generates_numbers = 100000 #variable for the amount of numbers generated
	generate_excel = 1 # 1 para generar excel y 0 para no generarlo
	matriz = Create_array(generates_numbers,4) #calling the function for the array creation depending rows and columns
	#Write Header File
	#text_head = 'n --- Xn ---  Xn+1 = (a * Xn + c)mod '+str(m)+' --- R=X/m'
	#Write_text_file('Gem.txt', text_head, 'w') # write first time File
	#Execute procces
	Exec_generates_numbers(generates_numbers)
	#print(matriz)
	#print(matriz[10][3])
	if generate_excel == 1:
		list_text_head = ["n", "Xn", "Xn+1 = (a * Xn + c)mod "+str(m), "R=X/m" ]
		#write_text_excel("gem","Gem con 100 datos", matriz, generates_numbers, 4, list_text_head)
		write_text_excel_openpyxl("gem","Gem con 100 datos", matriz, generates_numbers, 4, list_text_head)