
#function for a create array, depending on its rows and columns
def Create_array(rows, columns):
	matriz= [] #array declaration global
	#It is created according to the rows and columns
	for i in range(rows):
		matriz.append([""]* columns)
	return matriz
	#matriz[2][3]=1 #example allocation of value a matriz