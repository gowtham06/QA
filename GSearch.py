
#!/usr/bin/python2.4
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint
#import urllib2
from apiclient.discovery import build

def GSearch(query):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  
  #proxy
  #import socks
  #import socket
  #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "172.16.1.1", 8080)
  #socket.socket = socks.socksocket
  #import urllib2
  
  service = build("customsearch", "v1",
            developerKey="AIzaSyAqhblDB_Q_xW4JncTwIeWO6IDUIc11zXw")
  searchCount=10
  print 'Requesting google server for results...'
  res = service.cse().list(
      q=query,
      cx='008059104263673983177:lsdzw72xoyy',
      num=searchCount 
   ).execute()
#  pprint.pprint(res)
#  print res['snippet']
  temp = res['items'] # returns me a list with index 0
#  print temp
#  temp1 = temp[0] # assign list to a variable
#  print temp1['snippet'] # extract snippet from that variable
#  temp2 = temp[1]
#  print temp2['snippet']
#  print type(temp1['snippet'])

#  print '--------------------------------------'
  toReturn = list()
  for x in xrange(0, searchCount):
      temp1 = temp[x]
      temp1['snippet']
      toReturn.append(temp1['snippet'])
#      print temp1['snippet']
#      print '-------------------------------'
#if __name__ == '__GSearch__':
  return toReturn

print GSearch('Where is louvre museum located?')
print "Hello Google"