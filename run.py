from BrainfuckInterpreter import BrainfuckInterpreter
from tkinter import *
class GUI():
	def __init__(self, master):
		self.bfi = BrainfuckInterpreter()
		self.master = master
		self.master.minsize(width=700, height=450)
		self.master.geometry('800x550')
		master.title("Brainfuck interpreter")

		self.code_label = Label(master, text="Code")
		self.code_label.pack()

		self.code_entry = Text(master, height=15, width=80)
		self.code_entry.pack()

		self.input_label = Label(master, text="Standard input")
		self.input_label.pack()

		self.text_entry = Text(master, height=3, width=80)
		self.text_entry.pack()

		self.output_label = Label(master, text="Standard output")
		self.output_label.pack()

		self.text_out = Text(master, height=6, width=80)
		self.text_out.configure(state="disabled")
		self.text_out.pack()

		self.run_button = Button(master, text="Run", width=50, command=self.run)
		self.run_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def run(self):
		code = self.code_entry.get("1.0",'end-1c')
		text = self.text_entry.get("1.0",'end-1c')
		self.bfi.brainfuck_to_py(code)
		self.set_text_out(self.bfi.get_output(text))

	def set_text_out(self, text):
		self.text_out.configure(state="normal")
		self.text_out.delete('1.0', END)
		self.text_out.insert(INSERT, text)
		self.text_out.configure(state="disabled")



root = Tk()
root.iconbitmap("dl.ico")
gui = GUI(root)
root.mainloop()
