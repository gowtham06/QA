from ngram import *
from GSearch import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordsTiling import *
import nltk
import codecs
import string
import unicodedata
import sys
import copy
import operator
from firstRun import *
from constructFeature import *
import math
print 'Searching google..'
searchQuery = "Where is louvre museum located?"
searchQuery2 ="Who is president of India?"
#searchQuery3="news"
snippets = GSearch(searchQuery)
#snippets = GSearch(searchQuery1) 
#snippets = GSearch(searchQuery2) 
#snippets=GSearch(searchQuery3)

totalSnippets = len(snippets)
print totalSnippets
totalNGrams = list()
totalNGramsDic = dict()
# remove stop words
stopset = stopwords.words('english')

tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))

for x in range(0,totalSnippets):
  tokens=word_tokenize(snippets[x].lower())
  tokens = [w for w in tokens if not w in stopset]
  stringEntire = " ".join(tokens)
  stringEntire = stringEntire.translate(tbl)
  temp = NGram(stringEntire,3)
  totalNGrams.append(temp)

#print totalNGrams
for x in range(0,len(totalNGrams)):
  #print '----'
  temp = totalNGrams[x]
  for y in range(0,3):
    #print totalNGrams[x]
    temp1 = temp[y].split(',')
    #print temp1
    for z in range(0,len(temp1)):
      if(temp1[z] in totalNGramsDic):
        totalNGramsDic[temp1[z]]+=1
      else:
        totalNGramsDic[temp1[z]]=1

for key, value in totalNGramsDic.iteritems():
    print key, value
#print totalNGramsDic
print '-------------------------'
totalNGramsFinal = copy.deepcopy(totalNGramsDic)
for key1, value1 in totalNGramsDic.iteritems():
    for key2, value2 in totalNGramsDic.iteritems():
        result = Tiling(key1, key2)
#        print result + " -> "+ key1+" : "+key2
        if(result!=""):
	   #print result + " -> "+ key1+" : "+key2
           totalNGramsFinal.pop(key1,None)
           totalNGramsFinal.pop(key2,None)
           totalNGramsFinal[result]=value1+value2
print '-------------------------'
#totalNGramsFinal = dict(sorted(totalNGramsFinal.iteritems(), key=operator.itemgetter(1)))
totalNGramsFinal = sorted(totalNGramsFinal.items(), key=lambda x:x[1])

#print type(totalNGramsFinal[0])
for x in totalNGramsFinal:
    print x
    #for y in totalNGramsFinal[x]:
   # 	print (y,':',totalNGramsFinal[x][y])
    #print str(x[0]).encode('utf8') +" "+ str(x[1]).encode('utf8')
#pprint(totalNGramsFinal)

centroids = GetCentroid()
for key,value in centroids.iteritems():
    print key , " -> " , value

queryVector = constructFeature(searchQuery)
print "Query Vector: ", queryVector

minDist = 999999999999999;
queryClassLabel = "";
for key,centroid in centroids.iteritems():
    dist=math.sqrt(sum((queryVector[k] - centroid[k])**2 for k in centroid.keys()))
    if(dist<minDist):
        minDist=dist
        queryClassLabel=key
print "Query Class label: ", queryClassLabel

#print type(totalNGramsFinal[0])
listOfLabels=[]
for tupl in totalNGramsFinal:
    vector = constructFeature(tupl[0])
    minDist = 999999999999999;
    classLabel = "";
    for key,centroid in centroids.iteritems():
        dist=math.sqrt(sum((vector[k] - centroid[k])**2 for k in centroid.keys()))
        if(dist<minDist):
   	    minDist=dist
	    classLabel=key
    listOfLabels.append(classLabel)
#    print tupl, " label:", classLabel
indices = [i for i, x in enumerate(listOfLabels) if x == queryClassLabel]
#print indices
reducedNGrams = itemgetter(*indices)(totalNGramsFinal)
#for x in reducedNGrams:
#  print x
print "Original length: ", len(totalNGramsFinal)
print "Reduced length: ", len(reducedNGrams)
