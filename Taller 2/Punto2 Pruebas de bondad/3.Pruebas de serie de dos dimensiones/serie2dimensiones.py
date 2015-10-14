#===================Pruebas de Serie de 2 dimensiones=================
from arrayCreation import Create_array
from listPseudoRandom import Pseudo_random
import math


#=============#Temporary List for Test 
list_test = [0.33, 0.33, 0.9, 0.5, 0.6, 0.6, 0.7, 0.1, 0.7, 0.4]
#============#End Temporary Lists for Test 
list_pseudoRandom = []
frequency_table = [] 
chiQuadrate_table = []

#function for add the values of chiquadrate, according the chiquadrate table
def Add_values_X_calc(dimention_classes):
	result_X_calc = 0
	for i in range(1, int(dimention_classes) + 1):
		for k in range(1,int(dimention_classes) + 1):
			result_X_calc += chiQuadrate_table[i][k] 
	return result_X_calc


#Function for calculate the chiquadrate value
def Calculate_value_chiquadrate(FO, FE):
	return math.pow(FE - FO, 2) / FE 

#function for to calculate the chi quadrate values, according the frecuency table and FE value
def Calculate_chiquadrate_values(frequency_table, chiQuadrate_table, FE, dimention_classes):
	for i in range(1, int(dimention_classes) + 1):
		for k in range(1,int(dimention_classes) + 1):
			chiQuadrate_table[i][k] = Calculate_value_chiquadrate(frequency_table[i][k], FE)


#function for to write the ranges on the frequency table
def Write_ranges_table(accumulator_range, dimention_classes, table):
	table[0][0] = "0-0" # this is not taken into account 
	initial_number = "0" #variable that specify the number initial
	end_number = accumulator_range # variable that specify the end number 
	for i in range(int(dimention_classes)):
		table[i + 1][0] =  initial_number + "-" + str(end_number) #Writing numbers in the rows
		table[0][i + 1] =  initial_number + "-" + str(end_number) #Writing numbers in the columns
		initial_number = str(end_number)
		end_number = end_number + accumulator_range 
	return table

#function for to extract the position number of the row or the column, according the type_pos
def Extract_value(type_pos, i):
	if type_pos == 0:
		return str(frequency_table[i][0]).split('-') # Becomes the text in a list of two positions(example:'0-0.5' = ['0', '0.5']) and return
	if type_pos == 1:
		return str(frequency_table[0][i]).split('-') 

#function for to evaluate the position of datum according to the range.
#if type_pos = 0 then is row else, if type_pos= 1 then is column
def Evaluate_pos_rangeRows(datum, dimention_classes, type_pos):
	result_position = 0
	values_range=['0','0']
	for i in range(dimention_classes + 1):#adds 1, because not it count the first row(the value is zero)
		values_range = Extract_value(type_pos, i) # calling function for to extract the position number of the row or the column, according the type_pos
		if datum >= float(values_range[0]) and datum <= float(values_range[1]) : #esta generando el numero 1 aleatorio
			result_position = i # assign the position of the rows  the variable  result_position
	return result_position



#function for to calculate the values of the frequency table with the events happening together(pairs)
def Calculate_value_frequencyTable(dimention_classes,list_pseudoRandom):
	i = 0
	while i <= (len(list_pseudoRandom) - 1 ): # clicle 'for' for browse the list of pseudo random
		datum_row= list_pseudoRandom[i]
		datum_col = list_pseudoRandom[i + 1]
		i += 2
		pos_row = Evaluate_pos_rangeRows(datum_row, dimention_classes, 0)# calling funtion for to Extract position of row
		pos_column = Evaluate_pos_rangeRows(datum_col, dimention_classes, 1) #Calling function for Extract position of column
		frequency_table[pos_row][pos_column] += 1 #adds 1, the frequency table, according the position of the row and column 
 
#executing main 
if (__name__=="__main__"):
		#list_pseudoRandom = list_test #Temporary for tests
		n = 1200
		list_pseudoRandom = Pseudo_random(n,2)# Calling function for the  Creation of pseudo random numbers
		data_quantity = len(list_pseudoRandom) #variable for the data quantity pseudo random
		#data_quantity = 1200 # Temporary for test
		pairs_number = round (float (data_quantity ) / 2) # variable for the pairs number
		class_number = math.ceil (math.sqrt( pairs_number)) # variable for the classes number. Rounded with ceil		
		dimention_classes = math.ceil (math.sqrt( class_number)) # variable for the classes number that require each dimension
		accumulator_range = 1 / dimention_classes #variable for to accumulate the ranges, for build the ranges on the frequency table
		
		#=======begin test frecuency table=======================
	    #Temporary for test		
		#frequency_table = [ ['0-0', '0-0.2', '0.2-0.4', '0.4-0.6','0.6-0.8', '0.8-1'], ['0-0.2', 22, 31, 35, 27, 25], ['0.2-0.4', 30, 22, 23, 17, 34], ['0.4-0.6', 17, 18, 24, 27, 24], ['0.6-0.8', 22, 27, 16, 22, 30], ['0.8-1', 18, 17, 23, 19, 26]]
		#=======end test frecuency table=========================
		
		#==================================================================================================
		#codigo que hace parte del programa se puede comentar para mostrar el test
		frequency_table = Create_array(int(dimention_classes) + 1, int(dimention_classes) + 1) #Calling function for the Creation of the frequency table
		frequency_table = Write_ranges_table(accumulator_range, dimention_classes, frequency_table) # Calling function for to write the ranges on the frequency table	
		Calculate_value_frequencyTable(int(dimention_classes), list_pseudoRandom) #Calling function for to calculate the values of the frequency table with the events happening together(pairs)
		
		#===================================================================================================		
		FE = float(pairs_number) / float(class_number) # value of the expected frequency
		chiQuadrate_table = Create_array(int(dimention_classes) + 1, int(dimention_classes) + 1)#Calling function for the Creation of the chi quadrate table
		chiQuadrate_table = Write_ranges_table(accumulator_range, dimention_classes, chiQuadrate_table) # Calling function for to write the ranges on the chi quadrate table
		Calculate_chiquadrate_values(frequency_table, chiQuadrate_table, FE, dimention_classes)# Calling funtion for calculate the chi quadrate values, according the frequency table
		X_Calc = Add_values_X_calc(dimention_classes)
		print ("Valor del chi cuadrado calculado " + str(X_Calc))