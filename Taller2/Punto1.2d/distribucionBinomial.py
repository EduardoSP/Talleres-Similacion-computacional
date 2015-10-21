#=====Punto 1.2 d) Generacion de datos distribucion binomial (n=100, p=0.3) por el metodo de convulcion==========
from arrayCreation import Create_array
from writeFile import Write_text_file
from GEM import Generate_values_r

distribution_binomial_table=[] #array declaration global for the values of the binomial distribution 
#==================================================================================================
#for test
#temporary declaration for test of the values of r that were created by the GEM
"""
r= [0.0530374, 0.808378,0.903386, 0.538051,0.875958, 0.513395,
	0.932824, 0.261447, 0.879235, 0.456081, 0.851364, 0.566246, 
	0.926326, 0.648505, 0.0858267, 0.603867, 0.297316, 0.126606,
	0.990079, 0.367285, 0.693317, 0.125736, 0.434217, 0.300056,  0.8, 0.8, 0.1] 
"""	
#==================================================================================================
r = []
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

#function for calculate te binomial distribution by the method of convulsion
def Exec_distribution_bino_conv(n, p, rows_binomial):
	a = 0
	ini= 0
	end = n
	list_new = []
	for i in range(rows_binomial):
		list_new = r[ini : end]# make a list with the range of ini and end
		ini = end 
		end = ini + n
		for k in range(len(list_new)):
			if list_new[k] <= p: #iterate the lis for evaluate the p minors
				a +=1 #adds 1 if is minor
			distribution_binomial_table[i][0] = str(distribution_binomial_table[i][0]) + " " + str(list_new[k])
		distribution_binomial_table[i][1] = a
		a = 0
		list_new=[] # initializes the list(list_new)

#executing main 
if (__name__=="__main__"):
	#=====================================================
	#parameters
	#n= 6 # value of n for test
	#p = 0.7 # Parameter of p for test
	n = 6
	p = 0.7
	#=====================================================
	#rows_calc = 25 #for test
	rows_calc = 100000
	r = Generate_values_r(rows_calc) # value of r. receives the amount of data to generate
	#number of rows for binomial distribution calculate
	rows_binomial = num_rows_table(rows_calc, n) # calling function for calculate the number of rows for build the table 
	#print rows_binomial
	distribution_binomial_table = Create_array(rows_binomial,2)#calling function for array creation depending rows and colums
	Exec_distribution_bino_conv(n, p, rows_binomial) #calling function for calculate te binomial distribution by the method of convulsion
	print(distribution_binomial_table)







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