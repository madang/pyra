#!/usr/bin/python
#coding:utf-8
import json
import urllib
import pprint

def showsome(searchfor,site):
  query_string='site:'+site+' '+searchfor
  query = urllib.urlencode({'q': query_string})
  print '*** query ***'
  print query
  raw_input('anykey?')
  
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  print 'search response %s' % search_response
  search_results = search_response.read()
  
  print '*** search_results ***'
  pprint.PrettyPrinter(indent=4).pprint(search_results)
  raw_input('anykey?')
  
  results = json.loads(search_results)
  data = results['responseData']
  print "*** PRINTING DATA ***\n"
#  pprint.PrettyPrinter(indent=4).pprint(data)

  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']


site='vlada.net'
keyword='политолог'
showsome(keyword,site)
