#=====Punto 1.2 d) Generacion de datos distribucion binomial (n=100, p=0.3)==========
from arrayCreation import Create_array
from writeFile import Write_text_file
from GEM import Generate_values_r

distribution_binomial_table=[] #array declaration global for the values of the binomial distribution 
#temporary declaration for test of the values of r that were created by the GEM
r= [0.0530374, 0.808378,0.903386, 0.538051,0.875958, 0.513395,
	0.932824, 0.261447, 0.879235, 0.456081, 0.851364, 0.566246, 
	0.926326, 0.648505, 0.0858267, 0.603867, 0.297316, 0.126606,
	0.990079, 0.367285, 0.693317, 0.125736, 0.434217, 0.300056] 
#==================================================================================================

#function for calculate the number of rows for the binomial distribution 
def num_rows_table(amount_data_list, n):
# operation for mumber of rows of the table
	division = amount_data_list / n
	num_res = amount_data_list % n
	if num_res == 0:
		division = division
	else:
		division= division + 1
	return division


#executing main 
if (__name__=="__main__"):

	n= 6 # value of n
	p = 0.7 # Parameter of p
	#number of rows for binomial distribution calculate
	rows_calc = num_rows_table(24, n) # calling function for calculate the number of rows for build the table 
	print(rows_calc)






"""
Note
# operation for mumber of rows of the table
valor= 31
division = valor / 6
num_resido = valor % 6
if num_resido == 0:
	print(division)
else:
	print(division + 1)
"""