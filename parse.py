#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import requests

# test re for this url
testurl=r'http://4vlada.net/partii-lidery/yatsenyuk-nasha-tsel-zakon-ob-impichmente-i-otstavka-yanukovicha'
print "Test url: %s \n" % testurl
r=requests.get(testurl)
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
	
print article_string.encode('utf-8')
# save results for analysis
t_filename = 'res.txt'
with open(t_filename,'w+') as f:
	f.write(article_string.encode('utf-8'))

