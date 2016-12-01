def findNosClasses(file):
	inputfile=open(file)
	classes=[];
	for line in inputfile:
		classes.append(line.rstrip())
	uniqueClassesSet=set(classes);
	uniqueClassesList=list(uniqueClassesSet);
	#print uniqueClassesList[0]
	return uniqueClassesList