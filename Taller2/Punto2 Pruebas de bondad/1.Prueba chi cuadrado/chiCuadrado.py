#===Punto 2.1 Prueba Chi Cuadrado===
from arrayCreation import Create_array
from listPseudoRandom import Pseudo_random
import math

chi_quadrat_table=[]# Table for chi quadrat
list_pseudorandom=[]# list for the pseudorandom numbers

#Temporary function for tests FO. For to check process
def value_FO_temporary(list_parameters_FO_tempory):
	for i in range(10):
			chi_quadrat_table[i][1] = list_parameters_FO_tempory[i]		


#Function for to claculate the chi qaudrat(calculated value) (FE-FO)^2/FE
def Exec_calculate_chi_quadrat():
	calculated_value = 0
	for i in range(10):#'for' cycle to the number of rows
		FE = chi_quadrat_table[i][2]
		FO = chi_quadrat_table[i][1]
		chi_quadrat_table[i][3] = math.pow((FE-FO),2) / FE
		calculated_value += chi_quadrat_table[i][3] 
	return calculated_value 


#Function for to write the expected frecuency in the table 'chi_quadrat_table'
def Write_FE_chi_quadrat_table(FE):
	for i in range(10):
		chi_quadrat_table[i][2] = FE

#Function for to calculate the observed frequency according the ranges 
def Calculate_FO():
	#ranges: [0,0.1), [0.1,0.2), [0.2,0.3), [0.3,0.4), [0.4,0.5), [0.5,0.6), [0.6,0.7), [0.7,0.8), [0.9,1.0)
	for i in range(len(list_pseudorandom)):
		if 0 <= list_pseudorandom[i] < 0.1:
			chi_quadrat_table[0][1] += 1
		if 0.1 <= list_pseudorandom[i] < 0.2:
			chi_quadrat_table[1][1] += 1
		if 0.2 <= list_pseudorandom[i] < 0.3:
			chi_quadrat_table[2][1] += 1
		if 0.3 <= list_pseudorandom[i] < 0.4:
			chi_quadrat_table[3][1] += 1
		if 0.4 <= list_pseudorandom[i] < 0.5:
			chi_quadrat_table[4][1] += 1
		if 0.5 <= list_pseudorandom[i] < 0.6:
			chi_quadrat_table[5][1] += 1
		if 0.6 <= list_pseudorandom[i] < 0.7:
			chi_quadrat_table[6][1] += 1
		if 0.7 <= list_pseudorandom[i] < 0.8:
			chi_quadrat_table[7][1] += 1
		if 0.8 <= list_pseudorandom[i] < 0.9:
			chi_quadrat_table[8][1] += 1
		if 0.9 <= list_pseudorandom[i] < 1.0:
			chi_quadrat_table[9][1] += 1

#function for to write the ranges of the chi quadrat table 
def Write_range_chi_quadrat_table():
	chi_quadrat_table[0][0] = "0-0.1"
	chi_quadrat_table[1][0] = "0.1-0.2"
	chi_quadrat_table[2][0] = "0.2-0.3"
	chi_quadrat_table[3][0] = "0.3-0.4"
	chi_quadrat_table[4][0] = "0.4-0.5"
	chi_quadrat_table[5][0] = "0.5-0.6"
	chi_quadrat_table[6][0] = "0.6-0.7"
	chi_quadrat_table[7][0] = "0.7-0.8"
	chi_quadrat_table[8][0] = "0.8-0.9"
	chi_quadrat_table[9][0] = "0.9-1.0"



#executing main 
if (__name__=="__main__"):
	n = 100 #number of data
	class_number= math.sqrt(n)#number of classes
	FE= n / class_number #expected frequency
	list_pseudorandom = Pseudo_random(n,3)# Calling function for the  Creation of pseudo random numbers 
	chi_quadrat_table = Create_array(10,4)#Calling function for the Creation of table Chi quadrat
	Write_range_chi_quadrat_table()#calling function for with write the range of table Chi quadrat
	"""
	list_parameters_FO_tempory=[14, 6, 16, 6, 7, 14, 7, 8, 16, 6]# Temporarry list for to calculate test 
	value_FO_temporary(list_parameters_FO_tempory)#calling Temporary function for tests FO. For to check process
	"""
	Calculate_FO()#Calling function for to calculate the observed frecuency
	Write_FE_chi_quadrat_table(FE)#Calling function for to write the value of the expected frequency in the chi quadrat table
	calculated_value_chi_quadrat = Exec_calculate_chi_quadrat()#Calling function for the calculation of the chi quadrat(calculated value)
	print(chi_quadrat_table)
	print(calculated_value_chi_quadrat)