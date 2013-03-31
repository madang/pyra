#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import search
import parse

class Pyra_Gui:
	def __init__(self, parent):
		self.parent = parent #remember the parent of the instance
		
		self.rubrics = {}
		# ================ RUBRIC buttons FRAME =======================
		self.rubrics_frame = tk.LabelFrame(parent, text = u"Рубрики")
		self.rubrics_frame.pack(side = tk.LEFT, expand = "no", fill = "y")
		
		#~ # -----------------ADD SOME BUTTONS------------
		#~ butn_names = [u'Законодавча влада', \
			#~ u'Виконавча влада', \
			#~ u'Політика', 
			#~ u'Україна у світових \n кризових тенденціях', \
			#~ u'Ще шось']
		self.but = []
		#~ 
		#~ for butn_name in butn_names:
			#~ self._add_button(self.rubrics_frame, butn_name)
			
			
		
		# ================== THE PARMS FRAME ===========================
		self.parameters = tk.Frame(parent)#, text = u'Параметри')
		self.parameters.configure(width = 100)
		self.parameters.pack(side = tk.RIGHT, expand = "no") #, fill = "both")
		
		# ================== DATE OPTIONS SUBFRAME
		self.date_options = tk.LabelFrame(self.parameters, text = u'Період публікації')
		self.date_options.pack(side = tk.TOP)
		
		# ------------------ Add the start date entry ------------------
		self.start_date_frame = tk.Frame(self.date_options)
		self.start_date_frame.pack()
		self.start_date_label = tk.Label(self.start_date_frame, text = u"З")
		self.start_date_label.pack(side = "left", anchor  = "w")
		self.start_date = tk.Entry(self.start_date_frame)
		self.start_date.pack(side = "right", expand = "yes", fill="x", anchor = "e")
		
		# ------------------ Add the end date entry --------------------
		self.end_date_frame = tk.Frame(self.date_options)
		self.end_date_frame.pack()
		
		self.end_date_label = tk.Label(self.end_date_frame, text = u"До")
		self.end_date_label.pack(side = "left")
		
		self.end_date = tk.Entry(self.end_date_frame)
		self.end_date.pack(side = "right")
		
		
		# ------------------ Add a "four days" butn --------------------
		self.four_butn = tk.Button(self.date_options, text = u'4 дні')
		self.four_butn.pack(side = "left",anchor = "sw")
		
		# ------------------ Add a "one day button" --------------------
		self.day_butn = tk.Button(self.date_options, text = u'1 день')
		self.day_butn.pack(anchor = "se") 
		
		
		# ================== SEARCH OPTIONS SUBFRAME ====================
		t_width = 26
		
		self.search_options = tk.LabelFrame(self.parameters, text = u'Параметри пошуку')
		self.search_options.configure(width = 100)
		self.search_options.pack(side = tk.TOP)
		
		# ------------------ Sites label and text
		self.sites_label = tk.Label(self.search_options,text = u"Сайти")
		self.sites_label.pack(anchor = "w")
		
		self.sites = tk.Listbox(self.search_options)
		#~ self.sites.configure(height = 10,width=t_width)
		self.sites.pack()#expand = "yes", fill = "both")
		
		#------------------- Keyword label and text
		self.keywords_label = tk.Label(self.search_options, text = u"Ключові слова")
		self.keywords_label.pack(anchor = "w")
		
		self.keywords = tk.Listbox(self.search_options)
		#~ self.keywords.configure(height = 10,width=t_width)
		self.keywords.pack()#expand = "yes", fill = "both")
		
		
		# ================== THE MAIN FRAME ============================
		self.articles = tk.LabelFrame(parent, text = u'Статті')
		#~ self.articles.configure(width = 400, height = 300)
		self.articles.pack(side = tk.LEFT,expand = "yes", fill = "both")
		
		# ------------------ Add the Text widget -----------------------
		self.txt = tk.Text(self.articles)
		self.txt.pack(expand = "yes", fill = "both")
		
	def _add_button(self,target,text):
		self.but.append(tk.Button(target,text = text, 
			command = lambda
			arg1 = text:
			self._display_rubric(arg1)
			))
		self.but[-1].configure(height = 2,width = 20)
		#~ print dir( self.but[-1])
		self.but[-1].pack()
		
		
	def add_rubric(self,in_rubric):
		self.rubrics[in_rubric.name]=in_rubric
		self._add_button(self.rubrics_frame,in_rubric.name)
		
	def _display_rubric(self,in_rubric_name,update_links = False):
		print "I got: %s" % in_rubric_name.encode('utf-8')
		
		# get the rubric instance (copy,dics are immutable) using the name
		temp_rub = self.rubrics[in_rubric_name]
		
		for sit in temp_rub.sites:
			self.sites.insert(tk.END, sit)
			
		for k in temp_rub.kw:
			self.keywords.insert(tk.END, k)
			
		if not hasattr(temp_rub,'links'):
			temp_rub.update()
			
		# save the state of the rubric!
		self.rubrics[in_rubric_name] = temp_rub
		
		# display the contents of art_dic in the Text widget
		for art in temp_rub.links:
			self.txt.insert(tk.END,"="*40 + "\n")
			self.txt.insert(tk.END, art + "\n")
			self.txt.insert(tk.END, temp_rub.art_dic[art])

class Rubric:
	def __init__(self,name,sites_list = [],kw_list = []):
		self.name = name
		self.sites = sites_list
		self.kw = kw_list
		
		
	def update(self):
		self.links=[]
		for t_site in self.sites:
			for t_kw in self.kw:
				self.links+=search.startpage_parse(t_site,t_kw,'w')
					
		self.art_dic = {} #article dictionary
		for l in self.links:
			print l
			print type(l)
			#~ raw_input('>>>>>>')
			
			self.art_dic[l] = parse.parser(l)

rubric_economic = Rubric(u"Економіка", \
	["4vlada.net"], [u"политолог"])#"minprom.ua","www.pravda.com.ua","www.ukrinform.ua"], \
	#[u"политолог"]), u"партия",u"политика",u"флеш-мобы",u"акции протеста"])
	
root = tk.Tk()
#~ myapp=MyApp(root)
pyra_gui = Pyra_Gui(root)
pyra_gui.add_rubric(rubric_economic)

root.mainloop()
