import re
import random
def dataGrabber():
	directory="/home/gowtham/Desktop/RSL/Dataset/";
	#file_name="train_1000.label";
	file_name=[];
	#file_name=set({"train_1000.label","train_2000.label","train_3000.label"});
	file_name.append("train_1000.label");
	file_name.append("train_2000.label");
	file_name.append("train_3000.label");
	file_name.append("train_4000.label");
	file_name.append("train_5500.label");
	for k in xrange(0,len(file_name)):
		inputfile=open(directory+file_name[k]);
		#print inputfile
		array = []
		for line in inputfile:
		    array.append(line)
		inputfile.close()
		questionTag=[];
		question=[];
		questionContext=[];
		for i in xrange(0,len(array)):
			temp=re.split(":",array[i])
			questionTag.append(temp[0]);
			temp1=re.split(" ",temp[1]);
			questionContext.append(temp1[0]);
			str="";
			for j in xrange(1,len(temp1)):
				str=str+" "+temp1[j];
			question.append(str);
	with open(directory+"questionList.txt", 'a') as file:
	    for item in question:
	        file.write("{}".format(item))
	with open(directory+"questionContext.txt", 'a') as file:
	    for item in questionContext:
	        file.write("{}\n".format(item))
	with open(directory+"questionTag.txt", 'a') as file:
	    for item in questionTag:
	        file.write("{}\n".format(item))
	array=[];
	testFile=open(directory+"TREC_10.label");
	for line in testFile:
		print line
		array.append(line)
	testQuestionTag=[];
	testQuestion=[];
	testQuestionContext=[];
	#print array
	for i in xrange(0,len(array)):
		print array[i]
		temp=re.split(":",array[i]);
		print temp[0]
		testQuestionTag.append(temp[0]);
		temp1=re.split(" ",temp[1]);
		testQuestionContext.append(temp1[0]);
		str="";
		for j in xrange(1,len(temp1)):
			str=str+" "+temp1[j];
		testQuestion.append(str);
	with open(directory+"testQuestionList.txt", 'w') as file:
	    for item in testQuestion:
	        file.write("{}".format(item))
	with open(directory+"testQuestionContext.txt", 'w') as file:
	    for item in testQuestionContext:
	        file.write("{}\n".format(item))
	with open(directory+"testQuestionTag.txt", 'w') as file:
	    for item in testQuestionTag:
	        file.write("{}\n".format(item))
