#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import requests
import search

def parser(article_url):
	"""Pick a parser depending on the domain"""
	d = {u'4vlada.net':parse_4vlada_net}
	
	m = re.findall(ur'http://(.+?)/',article_url)
	print '*'*24
	print m
	
	key  = m[0]
	return d[key](article_url)

def parse_4vlada_net(article_url):
	"""parse an article from 4vlada.net v0.0 17-03-2013"""
	print "Article url: %s \n" % article_url
	r=requests.get(article_url)
	t_sensible_text = re.findall(ur'<p>(.+)</p>',r.text)
	article_string=u''
	if t_sensible_text:
		for i in t_sensible_text[0:-1]: # last match in the t_sensible_text list is useless
			#~ print i.encode('utf-8')
			article_string+=i+'\n'
	else:
		print "I got nothin'"
		
	# replace &quot; with "
	article_string = article_string.replace(u'&quot;',u'"')
	print '='*40
	print article_string.encode('utf-8')
	return article_string.encode('utf-8')
	# save results for analysis
	#~ t_filename = 'res.txt'
	#~ with open(t_filename,'w+') as f:
		#~ f.write(article_string.encode('utf-8'))

site = '4vlada.net'
keyword = u'политолог'
timeframe = 'w' # 'w' for last week, 'd' for yesterday

link_list = search.startpage_parse(site,keyword,timeframe)
print '*'*24
print link_list

parsed_article = []
for article in link_list:
	parsed_article.append(parser(article))
	
print '\n\n'.join(parsed_article)
