#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re

# OK, seem's like we've got a way to search without dealing with anally fenced off corporations
def startpage_parse(site,keyword):
	engine_url = 'https://startpage.com/do/search'
	q_string = 'host:' + site + ' ' + keyword
	payload = {'q' : q_string}
	r = requests.get(engine_url, params = payload)

	# Uncomment lines below to save the html
	#~ with open('res.html','w+') as out_file:
		#~ out_file.write(r.text.encode('utf-8'))
		
	links_list = re.findall(ur"<h3><a href=\'(.+)\' id",r.text)
	print '\n\n'.join(links_list)



cache_filename = 'cache.pk'
site = '4vlada.net'
keyword = 'политолог'

startpage_parse(site,keyword)
