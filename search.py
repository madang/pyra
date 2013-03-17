#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
from sys import exit


# OK, seem's like we've got a way to search without dealing with anally fenced off corporations
def startpage_parse(site,keyword,timeframe):
	if  timeframe not in ['d','w']:
		exit(1,'timeframe can be either "d" of "w", you supplied %s' % timeframe)
		
	engine_url = 'https://startpage.com/do/search'
	#~ q_string = 'host:' + site + ' ' + keyword
	payload = {'cat':'web',
		'atleast_one' : keyword,
		'with_domain' : site, 
		'with_date': timeframe}
	r = requests.get(engine_url, params = payload)
	print r.url
	# Uncomment lines below to save the html
	with open('res.html','wb+') as out_file:
		out_file.write(r.text.encode('utf-8'))
		
	links_list = re.findall(ur"<h3><a href=\'(.+)\' id",r.text)
	print '\n\n'.join(links_list)



cache_filename = 'cache.pk'
site = '4vlada.net'
keyword = u'политолог'
timeframe = 'w' # 'w' for last week, 'd' for yesterday

startpage_parse(site,keyword,timeframe)
