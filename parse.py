#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import requests
import search
import urlparse

def parser(article_url):
	"""Pick a parser depending on the domain v0.1 01-04-2013"""
	
	d = {u'4vlada.net':parse_4vlada_net,
		u'minprom.ua':parse_minprom_ua,
		u'www.pravda.com.ua':parse_www_pravda_com_ua,
		u'www.ukrinform.ua':parse_www_ukrinform_ua,
		u'iportal.rada.gov.ua':parse_iportal_rada_gov_ua}
		
	
	print '*'*24
	print 'article_url = %s' % article_url
	
	key  = urlparse.urlsplit(article_url).netloc
	
	if key not in d:
		return "%s : PARSER UNIMPLEMENTED" % key.encode('utf-8')
	r=requests.get(article_url)
	if not r.ok:
		return 1
		
	return d[key](r.text)

def parse_4vlada_net(in_text):
	"""parse an article from 4vlada.net v0.2 02-04-2013"""
	
	t_sensible_text = re.findall(ur'<p.+>(.+)</p>',in_text)
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


def parse_minprom_ua(in_text):
	"""parse an article from minprom.ua v0.1 01-04-2013"""
	
	t_sensible_text = re.findall(ur'<p id="font_size" class="text_art">(.+)</p>',in_text,re.DOTALL)
	print "len(t_sensible_text) = %d" % len(t_sensible_text)
	article_string = ''.join(t_sensible_text)
	print article_string
	raw_input(">>>>>>");
	print '='*40
	#~ print article_string.encode('utf-8')
	return article_string

def parse_www_pravda_com_ua(in_text):
	"""parse an article from www.pravda.ua v0.1 01-04-2013"""
	
	t_sensible_text = re.findall(ur'<p>(.+)</p>',in_text)
	print "len(t_sensible_text) = %d" % len(t_sensible_text)
	article_string = '\n'.join(t_sensible_text)
	raw_input(">>>>>>");
	print '='*40
	print article_string.encode('utf-8')
	return article_string


def parse_www_ukrinform_ua(in_text):
	"""parse an article from www.ukrinform.ua v0.1 01-04-2013"""
	t_sensible_text = re.findall(ur'<h1>(.+)<div class="clear">',in_text,re.DOTALL)
	#~ print "len(t_sensible_text) = %d" % len(t_sensible_text)
	article_string = '\n'.join(t_sensible_text)
	#~ raw_input(">>>>>>");
	#~ print '='*40
	#~ print article_string.encode('utf-8')
	return article_string
	
	
def parse_iportal_rada_gov_ua(in_text):
	t_sensible_text = re.findall(ur'lang="UK">(.+?)</span></p>',in_text,re.DOTALL)
	article_string = '\n'.join(t_sensible_text)
	return article_string
	#~ # save results for analysis
	#~ t_filename = 'res.txt'
	#~ with open(t_filename,'w+') as f:
		#~ f.write(article_string.encode('utf-8'))

def filter_blacklisted(in_text):
	"""check if the string contains blacklisted sources v0.0 01-04-2013
	returns True|False
	"""
	
	blacklist = [u"РБК-Украина",
		u"Интерфакс",
		u"УНИАН",
		u"Украинские новости",
		u"День", #TODO add html quotes here
		u"Cегодня" #TODO add html quotes here
		]
	blacklist_re = u"|".join(blacklist)
	m = re.search(blacklist_re,in_text,re.U)
	if m:
		return True
	else:
		return False

def parse_link_list(link_list):
	print '='*40
	print link_list

	out_dic ={}

	for article in link_list:
		out_dic[article] = parser(article)

	return out_dic

if __name__=="__main__":
	from sys import argv
	print argv
	if len(argv) != 4:
		print "parse.py: Usage:parse.py site keyword timeframe"
		raw_input("Press Ctrl-C or I will continue with args from the source code")
		 
		site = 'www.ukrinform.ua'
		keyword = u'политолог'
		timeframe = 'w' # 'w' for last week, 'd' for yesterday
	else:
		site, shell_keyword, timeframe = argv[1:]
		keyword = shell_keyword.decode('utf-8')
	link_list = search.startpage_parse(site,keyword,timeframe)
	t_dic =  parse_link_list(link_list)
	for t_a in t_dic:
		print "="*80
		print t_a.encode('utf-8')
		print "="*80
		print t_dic[t_a].encode('utf-8')
		print "\n"*2
