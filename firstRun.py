from dataGrabber import dataGrabber
from constructFeature import constructFeature
from append2File import append2File
from isStopWord import isStopWord
from findTotalNosClasses import findNosClasses
from learnParameters import learnParameters
from testData import testData
from listFiles import listFiles
import numpy as np
from operator import itemgetter
import operator
from collections import Counter

def GetCentroid():
	#dataGrabber()
	#constructFeature()
	#append2File("test","sample text");
	#learnParameters()
	uniqueClasses=findNosClasses("/home/vikki/RSL/Dataset/questionTag.txt")
	#print uniqueClasses
	testDataDirectory="/home/vikki/RSL/Dataset/";
	testDataFile="testQuestionList.txt"
	testDataTagFile="testQuestionTag.txt"
	returnSet = testData(testDataDirectory,testDataFile,testDataTagFile);
	#print returnSet[0]
	with open ("/home/vikki/RSL/Dataset/testQuestionTag.txt", "r") as myfile:
	    classes=myfile.read().splitlines()
	#print classes
	#print type(classes)
	#print len(classes)
	#returnSet = listFiles("/home/gowtham/Desktop/RSL/tempDataset/")
	centroids={};
	for c in uniqueClasses:
	  indices = [i for i, x in enumerate(classes) if x == c]
	  reducedList = itemgetter(*indices)(returnSet)
	  classList=findNosClasses("/home/vikki/RSL/Dataset/questionTag.txt");
	  temp=[0]*len(classList);
	  Sum=dict(zip(classList,temp))
	  for i in xrange(0,len(reducedList)):
	    A = Counter(Sum);
	    B = Counter(reducedList[i]);
	    Sum=dict(A+B)
	  for key, value in Sum.items():
	    Sum[key] = value / len(reducedList)
	  #centroids.append(Sum);
	  centroids[c]=Sum;
	return centroids
