from tkinter import *
import Pmw

class SLabel(Frame):
	"""SLabel defines a 2-sided label within a Frame. The
		left hand label has blue letters; the right has white letters."""
	def __init__(self, master, left1, right1):
		Frame.__init__(self, master, bg = 'gray40')
		self.pack(side = LEFT, expand = YES, fill = BOTH)
		Label(self, text = left1, fg = 'steelblue1',
			font = ("arial", 6 , "bold"), width = 5, bg = 'gray40').pack(
			side = LEFT, expand = YES, fill = BOTH)

		Label(self, text = right1, fg = 'gray40',
			font = ("arial", 6 , "bold"), width = 1, bg = 'gray40').pack(
			side = RIGHT, expand = YES, fill = BOTH)

class Key(Button):
	