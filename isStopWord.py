def isStopWord(str):
	searchFlag=None;
	stopWords=[]
	filename="stopWords.txt"
	inputfile=open(filename);
	for line in inputfile:
		stopWords.append(line)
	for i in xrange(0,len(stopWords)):
		stopWords[i]=stopWords[i].rstrip()
		if(stopWords[i]==str.rstrip().strip(" ")):
			searchFlag=True;
			break;
	# if searchFlag==True:
	# 	print "Stopword found"
	# else:
	# 	print "Stopword not found"
	return searchFlag

	