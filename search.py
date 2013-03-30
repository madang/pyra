#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
from sys import exit #someday redo to raise exception


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
	#~ print r.url
	assert r.ok
	# Uncomment lines below to save the html
	#~ with open('res.html','wb+') as out_file:
		#~ out_file.write(r.text.encode(r.encoding))
		
	links_list = re.findall(ur"<h3><a href=\'http://"+site+"(.+)\' id",r.text)
	links_out = []
	for link in links_list:
		links_out.append('http://'+site+link)
	return links_out
	#~ print '\n\n'.join(links_out)


## Commented code below was used to debug this  module when I was writing it 
## Gena

#~ cache_filename = 'cache.pk'
#~ site = 'minprom.ua'
#~ keyword = u'партия'
#~ timeframe = 'w' # 'w' for last week, 'd' for yesterday

#~ startpage_parse(site,keyword,timeframe)
