#===================Pruebas de Corridas (Crecimiento y por la media)=================
import math
from listPseudoRandom import Pseudo_random
#=============#Temporary Lists for Test 
list_data_Test1=[0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,
				0.84, 0.74, 0.73, 0.71, 0.53, 0.41, 0.31, 0.18, 0.16, 0.11,
				0.01, 0.09,0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,
				0.91, 0.88, 0.86, 0.68, 0.54, 0.38, 0.36, 0.29, 0.13, 0.12]

list_data_Test2=[0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36 , 0.27,
				0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
				0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
				0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29]

#============#End Temporary Lists for Test 

#function for to calculate the variance value
def Calculate_variance(n1, n2):
	return ( round( math.sqrt( float( (2 * n1 * n2) * ((2 * n1 * n2) - n1 - n2 ) ) / 
			float( (math.pow(n1 + n2, 2) * ( n1 + n2 -1) ) ) ), 2 ) )


#Function for to calculate the media value
def Calculate_media(n1, n2):
	return (  round ( ( (float(2*(n1*n2))) / float((n1+n2) ) ) + 1 , 2 )  ) 


#Function for to evaluate if is of growth or is by the average
def Comparation_Conditional(type_test, list_data, i):
	if type_test == 0:
		#Is Evaluation by growth 
		if list_data[i+1] >= list_data[i]:
			return True
		else:
			return False
	else:
		#Is Evaluation by average
		if list_data[i] >= 0.5:
			return True
		else:
			return False


#Function for to evaluate the list by growth and calculate the amount of runs
def Exec_evaluation_runs(list_data, list_runs, type_test, amount_runs, minus):
	list_runs = []# list of 'corridas' (+,-)
	flag_runs = 0 #If is zero, then is positive runs('corridas'), else if is one is negative runs('corridas')
	#result_function Save four results, where la firts position is the amount_runs, the second position is the amount of positives,
	# the third is the amount of negatives and last position is the amount of list_runs 
	result_function = []
	number_positives = 0
	number_negatives = 0
	for i in range(len(list_data)- minus): #if minus is zero because no campare the next, if is one compare the next
		if Comparation_Conditional(type_test, list_data, i): #calling function according if is by growth or average
			if flag_runs == 1: #if was runs negative
				amount_runs+=1	#one adds to amount_runs
			list_runs.append("+")
			number_positives +=1 #adds number of positives
			flag_runs = 0 #Transform positive runs
		else:
			if flag_runs == 0:#if was runs positive
				amount_runs+=1	#one adds to amount_runs
			list_runs.append("-")
			number_negatives +=1 #adds number of negatives
			flag_runs = 1 #Transform negative runs
	result_function.append(amount_runs)#position zero is amount_runs
	result_function.append(number_positives)#position one is number_positives
	result_function.append(number_negatives)#position two is number_negatives
	result_function.append(list_runs)#position three is list_runs
	return result_function

#executing main 
if (__name__=="__main__"):
	#======================================
	n = 100 #number of data for the pseudorandom
	#Note: the only thing that changes in the code. Value 0 or 1 for the test type
	type_test = 1 #if type_test=0 then is 'corrida por crecimiento' else if is type_test=1 then is 'corrida por media' 
	#======================================
	list_runs = []
	#list (result_function) for the results of the function 'Evaluation_runs' #position zero is amount_runs, 
	#position one is number_positives, position two is number_negatives and position three is list_runs
	result_function = [] 
	amount_runs = 0
	minus= 0 #value zero for test average
	mi = 0 #Variable for the media
	sigma = 0#variable for the variance

	if type_test == 0:
		#test of growth
		list_runs.append("*")#First position add *
		amount_runs = 1 #becouse no count first position
		minus = 1 #value one for test growth

	#result_function = Exec_evaluation_runs(list_data_Test2, list_runs, type_test, amount_runs, minus) #Test. class example
	#=================================================================================================
	list_pseudorandom = Pseudo_random(n,3)# Calling function for the  Creation of pseudo random numbers
	result_function = Exec_evaluation_runs(list_pseudorandom, list_runs, type_test, amount_runs, minus) 
	#=================================================================================================

	number_runs = result_function[0] #variable for the number of 'corridas'
	n1 = result_function[1] # number of '+'
	n2 = result_function[2]# number of '-'
	print(result_function)
	mi = Calculate_media(n1, n2) #calling function for to calculate the media
	sigma = Calculate_variance(n1, n2) #calling function for to calculate the variance
	print("number of 'corridas' is "+ str(number_runs))
	print("mi is "+ str(mi))
	print("sigma is "+ str(sigma))
