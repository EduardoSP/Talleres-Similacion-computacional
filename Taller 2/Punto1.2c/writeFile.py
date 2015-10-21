def Write_text_file(nameFile, text, type_write):
	#if type_write is 'a' overwrite
	#else if type_write is 'w' write first time
	outfile = open(nameFile, type_write)
	outfile.write(text+'\n')
	outfile.close()