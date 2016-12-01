def searchWord(file,word):
	searchFlag=None;
	inputfile=open(file);
	for line in inputfile:
		#print line.lower().rstrip()+","+word.lower()
		if(line.lower().rstrip()==word.lower()):
			#print word,"found in ", file
			searchFlag=True;
			#print "Found"
			break;
	return searchFlag
