#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pickle
import re

#https://startpage.com/do/search?q=startpage.com+API


# the function below gives only 4 result which sucs, don't use
def search_google_web_api(site, keyword, cache_filename):
	"""Don't use""" 
	try:
		in_file = open(cache_filename,'r')
		reply_json = pickle.load(in_file)
	except:
		engine_url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0'
		
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


# the function below is not finished, don't use
def search_google_parse():
	"""Don't use """
	# using saved result for testing purposes
	with open('google_response.html') as in_file:
		response_text = in_file.read();
	print response_text
	response_links = re.findall(ur'<h3(.+)</h3>',r.text)
	t_filename = 'res.txt'
	with open(t_filename,'w+') as f:
		f.write(response_links.encode('utf-8'))


# OK, seem's like we've got a way to search without dealing with anally fenced off corporations
def startpage_parse(site,keyword):
	engine_url = 'https://startpage.com/do/search'
	q_string = 'host:' + site + ' ' + keyword
	payload = {'q' : q_string}
	r = requests.get(engine_url, params = payload)
	#~ print r
	#~ print r.text
	with open('res.html','w+') as out_file:
		out_file.write(r.text.encode('utf-8'))
	links_list = re.findall(ur"<h3><a href=\'(.+)\' id",r.text)
	print '\n\n'.join(links_list)



cache_filename = 'cache.pk'
site = '4vlada.net'
keyword = 'политолог'

startpage_parse(site,keyword)
