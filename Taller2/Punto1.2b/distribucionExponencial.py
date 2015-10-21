#=====Punto 1.2 b) Generacion de datos distribucion exponencial con parametro lambda=2.1==========
from arrayCreation import Create_array
from writeFile import Write_text_file
from GEM import Generate_values_r
import math   # This will import math module

distribution_exponential_table=[] #array declaration global for the values of the exponential distribution 
#temporary declaration for test of the values of r that were created by the GEM
#r= [0.5520,0.4881,0.7512,0.3124,0.5696,0.7238,0.9438] 
r=[]

#function that calculates the value of 'a'. number_r being uniform zero and one
def Calculate_value_a(lambda_value, number_r):
	a = (-1/lambda_value)*math.log(number_r)
	return a

#function for procces the exponential distribution
def Exec_process_exponential_distribution(rows_calc, lambda_value):
	n=0
	while(n < rows_calc):
		#column r
		number_r = r[n]
		distribution_exponential_table[n][0]= number_r
		distribution_exponential_table[n][1] = Calculate_value_a(lambda_value, number_r)
		#write line by line File
		text_line = str(number_r) +' --- ' + str(distribution_exponential_table[n][1])
		Write_text_file('exponentialDistribution.txt', text_line, 'a') 	
		n = n + 1


#executing main 
if (__name__=="__main__"):
	#number of rows for normal distribution calculate
	#rows_calc = 7
	rows_calc = 100000
	r = Generate_values_r(rows_calc) # value of r. receives the amount of data to generate
	#r = Generate_values_r(rows_calc) # value of r. receives the amount of data to generate
	#Creation of size for array for the normal distribution 
	distribution_exponential_table = Create_array(rows_calc,2)#calling function for array creation depending rows and colums
	lambda_value = 1.5 # fixed value of the example. class slides(number 76) of value lambda 
	#Write Header File
	text_head = 'r --- a'
	Write_text_file('exponentialDistribution.txt', text_head, 'w') # write first time File 
	Exec_process_exponential_distribution(rows_calc, lambda_value)
	print("Distribucion exponecial generada")
	#print(distribution_exponential_table)