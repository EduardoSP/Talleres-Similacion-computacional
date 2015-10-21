#===Punto 2.1 Prueba Chi Cuadrado Version 2===
from arrayCreation import Create_array
from listPseudoRandom import Pseudo_random
import math

chi_quadrat_table=[]# Table for chi quadrat
list_pseudorandom=[]# list for the pseudorandom numbers

#function for to write the ranges on the frequency table
def Write_ranges_table(accumulator_range, class_number, table):
	table[0][0] = "0-0" # this is not taken into account 
	initial_number = "0" #variable that specify the number initial
	end_number = accumulator_range # variable that specify the end number 
	for i in range(int(class_number)):
		table[i][0] =  initial_number + "-" + str(end_number) #Writing numbers in the rows
		initial_number = str(end_number)
		end_number = end_number + accumulator_range 
	return table


#Temporary function for tests FO. For to check process
def value_FO_temporary(list_parameters_FO_tempory):
	for i in range(10):
			chi_quadrat_table[i][1] = list_parameters_FO_tempory[i]		


#Function for to claculate the chi qaudrat(calculated value) (FE-FO)^2/FE
def Exec_calculate_chi_quadrat(class_number):
	calculated_value = 0
	for i in range(int(class_number)):#'for' cycle to the number of rows
		FE = chi_quadrat_table[i][2]
		FO = chi_quadrat_table[i][1]
		chi_quadrat_table[i][3] = math.pow((FE-FO),2) / FE
		calculated_value += chi_quadrat_table[i][3] 
	return calculated_value 


#Function for to write the expected frecuency in the table 'chi_quadrat_table'
def Write_FE_chi_quadrat_table(FE, class_number):
	for i in range(int(class_number)):
		chi_quadrat_table[i][2] = FE

#Function for to calculate the observed frequency according the ranges 
def Calculate_FO(class_number):
	values_range=['0','0']
	for i in range(len(list_pseudorandom)):
		for k in range(int(class_number)):
			values_range = str(chi_quadrat_table[k][0]).split('-')
			datum = list_pseudorandom[i]
			if datum > float(values_range[0]) and datum <= float(values_range[1]):
				chi_quadrat_table[k][1] += 1 




#executing main 
if (__name__=="__main__"):
	n = 1200 #number of data
	class_number= math.ceil(math.sqrt(n))#number of classes
	FE= n / class_number #expected frequency
	accumulator_range = 1 / class_number #variable for to accumulate the ranges, for build the ranges on the frequency table
	#list_pseudorandom = [0.12, 0.134, 0.3, 0.5, 0.7, 0.9, 0.8, 0.93, 0.1, 0.4, 0] # Temporary list for test quantity data is 3
	list_pseudorandom = Pseudo_random(n,3)# Calling function for the  Creation of pseudo random numbers 
	chi_quadrat_table = Create_array(int(class_number), 4)#Calling function for the Creation of table Chi quadrat
	#list_parameters_FO_tempory=[14, 6, 16, 6, 7, 14, 7, 8, 16, 6]# Temporarry list for to calculate test 
	#value_FO_temporary(list_parameters_FO_tempory)#calling Temporary function for tests FO. For to check process
	chi_quadrat_table = Write_ranges_table(accumulator_range, class_number, chi_quadrat_table)
	Calculate_FO(class_number)#Calling function for to calculate the observed frecuency
	Write_FE_chi_quadrat_table(FE, class_number)#Calling function for to write the value of the expected frequency in the chi quadrat table
	calculated_value_chi_quadrat = Exec_calculate_chi_quadrat(class_number)#Calling function for the calculation of the chi quadrat(calculated value)
	#print(chi_quadrat_table)
	print("Valor calculado de chi cuadrado es "+ str(calculated_value_chi_quadrat))