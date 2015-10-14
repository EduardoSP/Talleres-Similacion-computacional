#===================Pruebas de Corridas (Crecimiento y por la media)=================

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

#Function for to evaluate the list by growth and calculate the amount of runs
def Evaluation_growth(list_data):
	list_runs = []# list of 'corridas' (+,-)
	list_runs.append("*") #First position add *
	flag_runs = 0 #If is zero, then is positive runs('corridas'), else if is one is negative runs('corridas')
	amount_runs = 1  # Is one because the first is * 
	#result_function Save four results, where la firts position is the amount_runs, the second position is the amount of positives,
	# the third is the amount of negatives and last position is the amount of list_runs 
	result_function = []
	number_positives = 0
	number_negatives = 0
	for i in range(len(list_data)-1):
		if list_data[i+1] >= list_data[i]: #Comparing if the next value is greater
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
	result_function.append(amount_runs)
	result_function.append(number_positives)
	result_function.append(number_negatives)
	result_function.append(list_runs)
	return result_function

#executing main 
if (__name__=="__main__"):
	print(Evaluation_growth(list_data_Test2))
