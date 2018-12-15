from importlib import reload
open("brainfuck_code.py", "w+")
import brainfuck_code as bfc

class BrainfuckInterpreter:
	def __init__(self, random_bf):
		self.random_bf = random_bf

	def brainfuck_to_py(self, code):
		comms = {
			">": "i = i + 1 if i < len(arr)-1 else 0",
			"<": "i = i - 1 if i > 0 else len(arr)-1",
			"+": "arr[i] = arr[i] + 1 if arr[i] != 255 else 0",
			"-": "arr[i] = arr[i] - 1 if arr[i] != 0 else 255",
			".": ["try: std_out += chr(arr[i])",
					"except ValueError: pass"],
			",": ["if text_pointer <= len(text)-1:", 
						"\tarr[i] = ord(text[text_pointer])",
						"\ttext_pointer += 1",
					"else: break"
				],
			"[": "while not arr[i] == 0:" 
		}
		if self.random_bf:
			comms["?"] = "arr[i] = round(random.uniform(0, 255))"

		inits = ['i=0', 'arr=[0]*30000', 'std_out=""', 'text_pointer=0']
		tabs = 0
		inloop = False
		with open("brainfuck_code.py", "w+") as f:
			f.write("import random\n")
			f.write("def get_std_out(text):" + "\n" + "\t")
			tabs +=1
			for c in inits:
				f.write(c + "\n" + "\t"*tabs)
			for c in code:
				if c in [',', '.']:
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
		return bfc.get_std_out(text.strip())

