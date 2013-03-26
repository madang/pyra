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
		self.parameters = tk.LabelFrame(parent, text = u'Параметри')
		#~ self.parameters.configure(width = 100)
		self.parameters.pack(side = tk.RIGHT, expand = "no", fill = "both")

		
		# ------------------ Add a butn
		self.time_butn = tk.Button(self.parameters, text = u'4 дні')
		self.time_butn.grid() #a little bit of inconsistency here, just experimenting
		
		
		# ================== THE MAIN FRAME ============================
		self.articles = tk.LabelFrame(parent, text = u'Статті')
		#~ self.articles.configure(width = 400, height = 300)
		self.articles.pack(side = tk.LEFT,expand = "yes", fill = "both")
		
		# ------------------ Add the Text widget
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
