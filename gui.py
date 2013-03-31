#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk

class Pyra_Gui:
	def __init__(self, parent):
		self.parent = parent #remember the parent of the instance
		
		
		# ================ RUBRIC buttons FRAME =======================
		self.rubrics_frame = tk.LabelFrame(parent, text = u"Рубрики")
		self.rubrics_frame.pack(side = tk.LEFT, expand = "no", fill = "y")
		
		# -----------------ADD SOME BUTTONS------------
		butn_names = [u'Законодавча влада', \
			u'Виконавча влада', \
			u'Політика', 
			u'Україна у світових \n кризових тенденціях', \
			u'Ще шось']
		self.but = []
		
		for butn_name in butn_names:
			self._add_button(self.rubrics_frame, butn_name)
			
			
		
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
		txt = tk.Text(self.articles)
		txt.pack(expand = "yes", fill = "both")
		
	def _add_button(self,target,text):
		self.but.append(tk.Button(target,text = text))
		self.but[-1].configure(height = 2,width = 20)
		#~ print dir( self.but[-1])
		self.but[-1].pack()



def report_event(event):
	"""Print a description of an event, base don its attributes.
	"""
	event_name = {"2": "KeyPress", "4": "ButtonPress"}
	print "Time", str(event.time)
	print "EventType=" + str(event.type), \
		event_name[str(event.type)], \
		"EventWidgetId=" + str(event.widget), \
		"EventKeySymbol=" + str(event.keysym)
		
root = tk.Tk()
#~ myapp=MyApp(root)
pyra_gui = Pyra_Gui(root)
root.mainloop()
