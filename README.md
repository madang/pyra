pyra
====

News aggregator in python

[current todo in progress]: write parsers for each site 

* exclude homepages from parsing (relevant at least for www.ukrinform.ua)

* add a function that would filter out articles containing blacklisted sources (like interfax, etc.)

* separate replacement of html markup (like quot) with their string counterparts into a separate function

==maybe==

* parse multiple pages from the search result (>10 articles per request)

* define the CLI interface spec

* imlement the CLI 
==done==
	
x read this http://docs.python-requests.org/en/latest/index.html (install and use Requests) 

x use re to parse a result from 4vlada.net in parse.py

x learn to get more than 4 results per API request (if fail just parse the darn thing)

x get search results as strings

x use proper encoding/decoding for unicode strings 

x build a tk gui
