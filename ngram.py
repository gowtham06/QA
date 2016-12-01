#!/usr/bin/python

import sys
#query = "hi this is praks";
def NGram(query,N):
  terms = query.split()
  #print terms[0]
  #print terms[1]
  #print terms[2]
  #print terms[3]
  querySize = len(terms)
  #print querySize
  #print terms
  
  result = list()
  #print result
  for k in range(1,N+1):
    #temp = list()
    temp=""
    for i in range(0,querySize-k+1):
  #    print terms[i:i+k]
      
      temp= temp+' '.join(terms[i:i+k])
      if(i!=querySize-k): 
        temp+=','
      #temp.append(terms[i:i+k])
  #  print temp
    result.append(temp)
  #print result
  return result

#if __name__ == "__NGram__":
  #print NGram(sys.argv[1:],sys.argv[2:])
#print NGram("hi this is praks",3)
