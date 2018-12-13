from importlib import reload
open("brainfuck_code.py", "w+")
import brainfuck_code as bfc

class BrainfuckInterpreter:
	def brainfuck_to_py(self, code):
		comms = {
			">": ["i+=1", "if i>len(arr)-1:", "\ti=0"],
			"<": ["i-=1", "if i<0:", "\ti=len(arr)-1"],
			"+": "arr[i] += 1",
			"-": "arr[i] -= 1",
			".": "std_out += chr(arr[i]-48)",
			",": ["if text_pointer > len(text)-1:", 
					"\tarr[i] = ord('0')",
					"\tbreak",
				"arr[i] = ord(text[text_pointer])+48",
				"text_pointer += 1"],
			"[": "while not arr[i] == ord('0'):" 
		}
		inits = ['i=0', 'arr=[48]*30000', 'std_out=""', 'text_pointer=0']
		tabs = 0
		inloop = False
		with open("brainfuck_code.py", "w+") as f:
			f.write("def get_std_out(text):" + "\n" + "\t")
			tabs +=1
			for c in inits:
				f.write(c + "\n" + "\t"*tabs)
			for c in code:
				if c == ">" or c == "<" or c == ",":
					for i in comms[c]:
						if not inloop and "break" in i:
							continue
						f.write(i + "\n" + "\t"*tabs)
					continue

				if c == "[":
					tabs += 1
					inloop = True
				elif c == "]":
					tabs -=1
					inloop = False
				f.write(comms.get(c, "") + "\n" + "\t"*tabs)

			f.write("return std_out")


	def get_output(self, text):
		reload(bfc)
		return bfc.get_std_out(text)

