#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pickle

cache_filename = 'cache.pk'

site = '' #'4vlada.net'
keyword = 'политолог'

try:
	in_file = open(cache_filename,'r')
	reply_json = pickle.load(in_file)
except:
	engine_url = url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0'
	
	query_string = ''.join(['site:',site,' ',keyword])
	payload = {'q':query_string}
	#~ print query_string
	r=requests.get(engine_url, params = payload)
	reply_json = r.json()
	with open(cache_filename,'w+') as output_file:
		pickle.dump(reply_json,output_file)

assert reply_json

#~ print reply_json
key0 = 'responseData'
reply_data = reply_json[key0]

key1 = 'results'
reply_results = reply_data[key1]

print len(reply_results)

for i in reply_results:
	print 
	print
