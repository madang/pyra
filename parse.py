#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import requests
import search

def parser(article_url):
	"""Pick a parser depending on the domain"""
	d = {u'4vlada.net':parse_4vlada_net, \
	u'minprom.ua':parse_minprom_ua, \
	u'www.pravda.com.ua':parse_www_pravda_com_ua, \
	u'www.ukrinform.ua':parse_www_ukrinform_ua}
	
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
	return article_string


def parse_minprom_ua(article_url):
	"""parse an article from minprom.ua v0.0 30-03-2013"""
	print "Article url: %s \n" % article_url
	r=requests.get(article_url)
	#~ print type(r.text)
	t_sensible_text = re.findall(ur'<p id="font_size" class="text_art">(.+)</p>',r.text,re.DOTALL)
	print "len(t_sensible_text) = %d" % len(t_sensible_text)
	article_string = ''.join(t_sensible_text)
	print article_string
	raw_input(">>>>>>");
	print '='*40
	#~ print article_string.encode('utf-8')
	return article_string

def parse_www_pravda_com_ua(article_url):
	"""parse an article from www.pravda.ua v0.0 30-03-2013"""
	print "Article url: %s \n" % article_url
	r=requests.get(article_url)
	t_sensible_text = re.findall(ur'<p>(.+)</p>',r.text)
	print "len(t_sensible_text) = %d" % len(t_sensible_text)
	article_string = '\n'.join(t_sensible_text)
	raw_input(">>>>>>");
	print '='*40
	print article_string.encode('utf-8')
	return article_string


def parse_www_ukrinform_ua(article_url):
	"""parse an article from www.ukrinform.ua v0.0 30-03-2013"""
	print "Article url: %s \n" % article_url
	r=requests.get(article_url)
	t_sensible_text = re.findall(ur'<h1>(.+)<div class="clear">',r.text,re.DOTALL)
	print "len(t_sensible_text) = %d" % len(t_sensible_text)
	article_string = '\n'.join(t_sensible_text)
	raw_input(">>>>>>");
	print '='*40
	print article_string.encode('utf-8')
	return article_string
	
	#~ # save results for analysis
	#~ t_filename = 'res.txt'
	#~ with open(t_filename,'w+') as f:
		#~ f.write(article_string.encode('utf-8'))


site = 'www.ukrinform.ua'
keyword = u'политолог'
timeframe = 'w' # 'w' for last week, 'd' for yesterday

link_list = search.startpage_parse(site,keyword,timeframe)
print '='*40
print link_list

parsed_article = []
## ============== in link_list[0] only for debugging purposes, change back for production
for article in link_list:
	parsed_article.append(parser(article))
	
print '\n\n'.join(parsed_article)
