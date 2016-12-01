def learnParameters():
	from os import listdir
	from os.path import isfile, join
	from isStopWord import isStopWord
	from searchWord import searchWord
	from append2File import append2File
	import re
	DomainFileDirectory="/home/gowtham/Desktop/RSL/tempDataset/"
	DataFileDirectory="/home/gowtham/Desktop/RSL/Dataset/"
	questionFile="questionList.txt"
	questionContextFile="questionContext.txt"
	#print "Hello World"
	questions=[]
	inputfile=open(DataFileDirectory+questionFile);
	for line in inputfile:
		questions.append(line)
	questionContext=[];
	inputfile=open(DataFileDirectory+questionContextFile);
	for line in inputfile:
		questionContext.append(line)
	count=0;
	for i in xrange(0,len(questions)):
		str=re.split(" ",questions[i]);
		currentContext=questionContext[i].rstrip()
		for j in xrange(0,len(str)):
			if(isStopWord(str[j])==None):
				if(searchWord(DomainFileDirectory+currentContext,str[j])==None):
					count=count+1;
					print count
					append2File(DomainFileDirectory+currentContext,str[j])



		