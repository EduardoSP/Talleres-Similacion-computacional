#==============Punto 1.2 a) Generacion de datos distribucion normal estandarizada===========
from arrayCreation import Create_array
from writeFile import Write_text_file
from GEM import Generate_values_r

interval_table= [] #array declaration global for the intervals 
distribution_normal_table=[]

#temporary declaration for test of the values of r that were created by the GEM
#r= [0.5520,0.4881,0.7512,0.3124,0.5696,0.7238,0.9438] 
r=[]#list for saving the values of r

#function for calculate the value of 'a'
def Calculate_value_a(lambda_value, Xk):
	a= (lambda_value * Xk) + (1 - lambda_value) * (Xk + 1)
	return a


#funtion for calculate el lambda value
def Calculation_lambda_value(x, number_r, y):
	lambda_value = (x - number_r) / (x - y) # Operation for calculate the lambda value
	return lambda_value

# function for the evaluation of the r interval (r with  interval the table) and calculate the lambda 
#and return interval a
def Calculate_intervals(number_r):
	#saving  the result in position zero the string, position one the value lambda an position two 
	#string interval a, in the position three the Xk 
	result_intervals=["", 0, "", 0] 
	for i in range(len(interval_table)-1):
		#compare if the number_r this in the range. If is true then concatenate the intervals and calculate lambda value
		if interval_table[i][1] <= number_r and number_r <= interval_table[i+1][1]:
			#interval r
			result_intervals[0]= "[" + str(interval_table[i][1]) + " , " + str(interval_table[i+1][1])+"]"
			#value of the lambda value
			result_intervals[1]= Calculation_lambda_value(interval_table[i+1][1], number_r, interval_table[i][1])
			#interval a
			result_intervals[2]= "[" + str(interval_table[i][0]) + " , " + str(interval_table[i+1][0])+"]"
			#value of Xk
			result_intervals[3]= interval_table[i][0] 
	return(result_intervals)



#function for procces the normal distribution
def Exec_process_normal_distribution(rows_calc):
	n=0 #Especific the amount data
	result_intervals_r=[]# saving  the result of the function Exec_evaluation_interval_r
	while(n < rows_calc):
		#column r
		number_r = r[n]
		#interval r
		distribution_normal_table[n][0] = number_r
		#interval of r
		result_intervals= Calculate_intervals(number_r)
		distribution_normal_table[n][1] = result_intervals[0]
		#lambda value
		distribution_normal_table[n][2] = result_intervals[1]
		#interval de a
		distribution_normal_table[n][3] = result_intervals[2]
		#calling function Calculate_value_a where result_intervals[1] is lambda_vaue and Xk is result_intervals[3]
		distribution_normal_table[n][4] = Calculate_value_a(result_intervals[1], result_intervals[3])
		#write line by line File
		text_line = str(distribution_normal_table[n][0]) +' --- '+ str(distribution_normal_table[n][1]) + ' --- '+ str(distribution_normal_table[n][2]) + ' --- '+ str(distribution_normal_table[n][3]) + ' --- '+  str(distribution_normal_table[n][4]) 
		Write_text_file('normalDistribution.txt', text_line, 'a') 	 
		n = n + 1

#executing main 
if (__name__=="__main__"):
	#Table of points for the intervals
	interval_table= [[-3, 0.0013], [-2, 0.0228], [-1, 0.1586], [0, 0.5], [1, 0.8413], [2, 0.9772], [3, 0.9987]]
	#number of rows for normal distribution calculate
	#rows_calc = 7 
	rows_calc = 100000
	r = Generate_values_r(rows_calc) # value of r. receives the amount of data to generate
	#Creation of size for array for the normal distribution 
	distribution_normal_table = Create_array(rows_calc,5)#calling function for array creation depending rows and colums
	#Write Header File
	text_head = 'r --- Intervalo de r --- Lambda --- Intervalo de a --- a  '
	Write_text_file('normalDistribution.txt', text_head, 'w') # write first time File
	Exec_process_normal_distribution(rows_calc)#calling function of the process of the normal distribution
	print("Distribucion normal estadarizada generada")