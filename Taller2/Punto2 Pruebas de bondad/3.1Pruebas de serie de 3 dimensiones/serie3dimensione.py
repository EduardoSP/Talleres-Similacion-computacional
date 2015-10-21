#===================Pruebas de Serie de 3 dimensiones=================

from arrayCreation import Create_array
from listPseudoRandom import Pseudo_random
import math

#======begin list for test=================
list_test = [0.33, 0.33, 0.9, 0.5, 0.6, 0.6, 0.7, 0.1, 0.7]
#======end list for test===================
list_pseudoRandom = []
frequency_table3 = []
list_subintervals = []
list_result_evaluation = []
list_triplets = []
chi_quadrate_table3 = []

#Function for calculate the chiquadrate value
def Calculate_value_chiquadrate(FO, FE):
	return math.pow(FE - FO, 2) / FE 

#function for calculate the chi quadrate values, according the FE
def Calculate_values_chiQuadrateTable(total_classes, FE): 
	result_chi_Calc = 0
	for i in range(total_classes):
		chi_quadrate_table3[i][1] = Calculate_value_chiquadrate(frequency_table3[i][1], FE)
		result_chi_Calc += chi_quadrate_table3[i][1]
	return result_chi_Calc # return the value of chi quadrate calculate


#function for to calculate the FO value
def Calculate_FO_frequeccyTable(total_classes):
	for i in range(len(list_triplets)):
		for k in range(total_classes):
			if frequency_table3[k][0] == list_triplets[i]:
				frequency_table3[k][1] += 1 

# function for to form one list of triplest, accordinf the Evaluate_range_values 
def Form_triplet():
	i = 0
	while i < len(list_result_evaluation):
		if i == len(list_result_evaluation) - 1 or i == len(list_result_evaluation) - 2 :
			#It does not take into account the latest  two data, becouse the latest not is triplet
			break
		list_triplets.append(str(list_result_evaluation[i]) +"-"+str(list_result_evaluation[i+1]) + "-" + str(list_result_evaluation[i+2])) 
		i += 3 # group it of three
#function for to evaluate the ranges according the values
def Evaluate_range_values():
	values_range=['0','0']
	for i in range(len(list_pseudoRandom)):
		for k in range(len(list_subintervals)):
			values_range = str(list_subintervals[k]).split('-')
			if float(list_pseudoRandom[i]) >= float(values_range[0]) and float(list_pseudoRandom[i]) < float(values_range[1]):
				list_result_evaluation.append( k + 1 ) 

# function for to write the ranges on the table(example: 1-1-1)
def Write_classes_table(intervals_group, table):
	intervals_group += 1 # begin in 1 the interval
	cont = 0
	for i in range(1, intervals_group):
		for j in range(1, intervals_group):
			for k in range(1, intervals_group):
				table[cont][0] = str(i) +"-"+str(j)+"-"+str(k)
				cont +=1
	return table

#function for to write the ranges on the list_subintervals or subintervals
def Write_subintervals_list(accumulator_range, intervals_group):
	initial_number = "0" #variable that specify the number initial
	end_number = accumulator_range # variable that specify the end number 
	for i in range(int(intervals_group)):
		list_subintervals.append(initial_number + "-" + str(end_number)) #Writing numbers of the range in the list
		initial_number = str(end_number)
		end_number = end_number + accumulator_range 

#executing main 
if (__name__=="__main__"):
	#list_pseudoRandom = list_test # temporary list for test

	n = 1200 #quantity of data

	list_pseudoRandom = Pseudo_random(n,2)# Calling function for the  Creation of pseudo random numbers

	triplets = math.ceil( float(n) / 3) # variable for the triplets number
	use_classes = math.ceil( math.sqrt(triplets) )
	pot = float(1) / 3 # variable for the potency. Help For the cubic root
	intervals_group = math.ceil( math.pow( use_classes, pot ) )# interval for each dimension
	total_classes = math.ceil( math.pow(intervals_group, 3) ) # Resulting number of classes
	accumulator_range = 1 / intervals_group #variable for to accumulate the ranges, for build the ranges on the frequency table
	FE = float(triplets) / total_classes # value of FE
	
	frequency_table3 = Create_array(int(total_classes) , 2) #Calling function for the Creation of the frequency table
	Write_subintervals_list(accumulator_range, intervals_group)#calling function for to write the ranges on the list_subintervals or subintervals
	frequency_table3 = Write_classes_table(int(intervals_group), frequency_table3) # calling function for to write the ranges on the table(example: 1-1-1)
	Evaluate_range_values() # calling function for to evaluate the ranges according the values
	Form_triplet()# calliing function for to form one list of triplest, accordinf the Evaluate_range_values 
	Calculate_FO_frequeccyTable(int(total_classes)) # calling function for to calculate the FO value
	
	chi_quadrate_table3 = Create_array(int(total_classes) , 2) #Calling function for the Creation of the chi quadrate table
	chi_quadrate_table3 = Write_classes_table(int(intervals_group), chi_quadrate_table3) # calling function for to write the ranges on the table(example: 1-1-1)
	result_chi_Calc = Calculate_values_chiQuadrateTable(int(total_classes), FE) # calling function for calculate the chi quadrate values, according the FE
	
	#print list_subintervals
	#print list_result_evaluation
	#print frequency_table3
	#print chi_quadrate_table3
	print("valor chi Calc es "+ str(result_chi_Calc))