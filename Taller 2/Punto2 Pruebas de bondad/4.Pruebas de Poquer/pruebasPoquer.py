#===================Pruebas de poquer (3 decimales)=================
import math
from arrayCreation import Create_array
from listPseudoRandom import Pseudo_random
#=============#Temporary List for Test 
list_Test = [0.959, 0.713, 0.178, 0.427, 0.299, 0.153, 0.087, 0.615, 0.188, 0.972,
			0.239, 0.425, 0.372, 0.015, 0.316, 0.532, 0.216, 0.466, 0.808, 0.444,
			0.084, 0.577, 0.166, 0.182, 0.904, 0.296, 0.854, 0.317, 0.051, 0.229,
			0.299, 0.199, 0.185, 0.222, 0.954, 0.582, 0.283, 0.324, 0.913, 0.158] 
#============#End Temporary Lists for Test 

chi_quadrat_table = [] # Table for chi quadrate

#Function for calculate the chiquadrate value
def Calculate_value_chiquadrate(FO, FE):
	return round( (math.pow(FE - FO,2)) / FE, 3 ) 


#==========================Inicio Funciones para probabilidad pendientes para revision====
#Nota: Aclarar estos calculos de probabilidad
#function for to calculate the probability '3 equals' 
def Probability_3equal():
	return 10 / math.pow(10, 3)

#function for calculate the probability '2 equals and 1 different'
def Probability_2equal_1different():
	return (10 * 9 * 3) / math.pow(10, 3)
#function for calculate the probability '3 differents'
def Probability_3differents():
	return (10 * 9 * 8) / math.pow(10, 3)

#==========================Fin Funciones para probabilidad pendientes para revision===

#function for to calculate the observed frecuency of the poquer test. with 3 decimals
def FO_poquer(list_secuence):
	# (list_results)list for to save the results of three equal(position 0), two equal(position 1) and three different(position 2)
	list_results= [0, 0, 0]
	for i in range(len(list_secuence)):
		decimal_str =str(list_secuence[i])
		if len(decimal_str) == 3 or len(decimal_str) == 4: # longitud no alcanza 3 decimales 
			decimal_str = decimal_str + "0" + "0" #To complete zero
		value1 =decimal_str[decimal_str.find(".") + 1]# Take the first decimal point after
		value2 =decimal_str[decimal_str.find(".") + 2]#Take the second decimal point after
		value3 =decimal_str[decimal_str.find(".") + 3]#Take the third decimal point after
		if value1 == value2 and value1 == value3: #adds the 1 if all values are equal 
			list_results[0]+=1
		else:
			if value1 == value2 or value2 == value3 or value1 == value3:
				list_results[1]+=1 # adds the 1 if at least two decimals are equal
			else:
				if value1 != value2 and value1 != value3: 
					list_results[2]+=1 # adds the 1 if the decimals are differents 
	return list_results


#executing main 
if (__name__=="__main__"):
	k = 3 # variable for the count of decimals
	n = 40 #Number of data
	chi_quadrat_table = Create_array(3,4)#Calling function for the Creation of table Chi quadrat
	#============== Begin. Naming class values =================
	chi_quadrat_table[0][0] = "3 iguales"
	chi_quadrat_table[1][0] = "2 iguales y 1 diferente"
	chi_quadrat_table[2][0] = "3 diferentes"
	#==============End. Naming class values ====================

	#============== Begin. Assigning FO values ====================
	#list_results=FO_poquer(list_Test)	#For Test of class slides
	list_pseudorandom = Pseudo_random(n,2)# Calling function for the  Creation of pseudo random numbers
	list_results=FO_poquer(list_pseudorandom)
	chi_quadrat_table[0][1] = list_results[0] #Assigning value FO of 'three equal'
	chi_quadrat_table[1][1] = list_results[1] # Assigning value FO of 'two equal'
	chi_quadrat_table[2][1] = list_results[2] #Assigning value FO of 'three different'	
	#============== End. Assigning FO values ======================

	#============== Begin. Assigning FE values ====================
	chi_quadrat_table[0][2] = Probability_3equal() * n  #Assigning value FE of 'three'
	chi_quadrat_table[1][2] = Probability_2equal_1different() * n # Assigning value FE of 'two equal'
	chi_quadrat_table[2][2] = Probability_3differents() * n #Assigning value FE of 'three different'	
	#============== End. Assigning FE values ======================

	#============== Begin. Assigning chi quadrate values ====================
	#Nota con la lista prueba no concuerda con los datos, quizas este mal la diapositiva preguntar al profesor
	chi_quadrat_table[0][3] = Calculate_value_chiquadrate(list_results[0], Probability_3equal() * n)  #Assigning value FE of 'three'
	chi_quadrat_table[1][3] = Calculate_value_chiquadrate(list_results[1], Probability_2equal_1different() * n)  # Assigning value FE of 'two equal'
	chi_quadrat_table[2][3] = Calculate_value_chiquadrate(list_results[2], Probability_3differents() * n)  #Assigning value FE of 'three different'	
	#============== End. Assigning chi quadrate values ======================
	Xcalc = chi_quadrat_table[0][3] + chi_quadrat_table[1][3] + chi_quadrat_table[2][3] 
	print(chi_quadrat_table)
	print("Valor Xcalc " + str(Xcalc))

#Nota:
#Nota con la lista prueba no concuerda con los datos, quizas este mal la diapositiva preguntar al profesor
#la operacion chi cuadrado da diferente diapositiva 69
 


