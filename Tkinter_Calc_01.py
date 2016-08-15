from tkinter import *

def frame(root, side):
	w = Frame(root)
	w.pack(side = side, expand = YES, fill = BOTH)
	return w

def button(root, side, text, command = None):
	w = Button(root, text = text,command = command)
	w.pack(side = side,expand = YES, fill = BOTH)
	return w

class Calculator(Frame):
	"""Simple Calculator"""
	def __init__(self):
		Frame.__init__(self)
		self.pack(expand = YES, fill = BOTH)
		self.master.title("Simple Calculator")
		self.master.iconname("calc1")

		display = StringVar()
		Entry(self, relief = SUNKEN, 
			textvariable = display).pack(side = TOP, expand = YES, 
									fill = BOTH)

		for key in ("123", "456", "789", "-0."):
			keyF = frame(self, TOP)
			for char in key:
				button(keyF, LEFT, char, 
					lambda w = display, s = '%s'%char: w.set(w.get() + s))

		opsFA = frame(self, TOP)

		for char in "+*":
			btn = button(opsFA, LEFT, char, 
				lambda w = display, c = char: w.set(w.get() + " " + c + " "))


		opsFB = frame(self, TOP)

		for char in "-/":
			btn = button(opsFB, LEFT, char, 
				lambda w = display, c = char: w.set(w.get() + " " + c + " "))

		opsFC = frame(self, TOP)
		btn = button(opsFC, LEFT, "=")
		btn.bind('<ButtonRelease-1>',lambda e, s = self, w = display: s.calc(w))

		btn = button(opsFC, LEFT, "C",lambda w = display: display.set(""))

	def  calc(self, display):
		try:
			display.set(eval(display.get()))
		except ValueError:
			display.set("ERROR")
		except ZeroDivisionError:
			display.set("Math Error")
		
if __name__ == '__main__':
	Calculator().mainloop()