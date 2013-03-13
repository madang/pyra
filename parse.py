#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import requests
# test re for this url
testurl=r'http://4vlada.net/vlast/kuzmin-vozomnil-sebya-komissarom-kattani'
print "Test url: %s \n" % testurl
r=requests.get(testurl)
t_sensible_text = re.findall(ur'<p>(.+)</p>',r.text)
if t_sensible_text:
	for i in t_sensible_text:
		print i.encode('utf-8')
		print
else:
	print "I got nothin'"
