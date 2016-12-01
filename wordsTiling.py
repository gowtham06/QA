from llist import sllist, sllistnode
def findPos(text1_list,x):
	#print "The x is :"
	text1_iterator=text1_list.first
	findFlag=0;
	while (text1_iterator!=None):
		#print "test 1"
		if (text1_iterator.value==x.value):
			#print text1_iterator.value
			findFlag=1;
			break;
		else:
			text1_iterator=text1_iterator.next
	if (findFlag==1):
		#print text1_iterator.value
		return text1_iterator
	else:
		#print "Not found"
		return None
def Join(text1_list,text2_list):
	resultList=sllist()
	text1_iterator=text1_list.first
	text2_iterator=findPos(text2_list,text1_iterator)
	listFlag=0
	insertFlag=1
	if(text2_iterator!=None):
		while (text2_iterator!=None and text1_iterator!=None):
			#print "test 2"
			x_value=text2_iterator.value
			y_value=text1_iterator.value
			if(x_value!=y_value):
				insertFlag=0
				break
			else:
				text1_iterator=text1_iterator.next
				text2_iterator=text2_iterator.next

		if (text1_iterator!=None and insertFlag!=0):
			resultList=text2_list
			while(text1_iterator!=None):
				resultList.append(text1_iterator.value)
				text1_iterator=text1_iterator.next
	return resultList


def Tiling(text1,text2): #return "Empty" if tiling is not possible
	resultantString=""
	text1_words=text1.split(" ")
	text2_words=text2.split(" ")
	text1_list=sllist()
	text2_list=sllist()
	resultList1=sllist()
	resultList2=sllist
	for i in range(len(text1_words)):
		text1_list.append(text1_words[i])
	for i in range(len(text2_words)):
		text2_list.append(text2_words[i])
	resultantString1=""
	resultantString2=""
	resultList1=Join(text1_list,text2_list)
	resultList2=Join(text2_list,text1_list)
	if(resultList1.size!=0):
		for i in resultList1:
			resultantString1=resultantString1+i
			resultantString1=resultantString1+" "
	else:
		resultantString1=""
	#------------------------
	if(resultList2.size!=0):
		for i in resultList2:
			resultantString2=resultantString2+i
			resultantString2=resultantString2+" "
	else:
		resultantString2=""
	if(len(resultantString1)>len(resultantString2)):
		return resultantString1
	elif(len(resultantString2)>len(resultantString1)):
		return resultantString2
	else:
		return ""
	
	
#def main():
#	text1="Hai how are you"
#	text2="am fine aw"
#	text3="Hi this is"
#	text4="this is Gowtham Kannan"
#	text5="this is not a way"
#	text6="GKB this is"
#	text7="you and what doing"
#	text8="Hi how are you"
#	print Tiling(text1,text2)
#	print Tiling(text3,text4) #call the finction Tiling(text1,text2) for doing Tilng where text1 and text2 are 2 n-grams in our case 
#	print Tiling(text5,text6)
#	print Tiling(text7,text8)
	
#if __name__ == "__main__":
#    main()	
