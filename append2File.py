def append2File(file,str):
	with open(file, "a") as myfile:
		myfile.write("\n"+str.lower());