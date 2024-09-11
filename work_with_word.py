import j2
import keyboard
import jconfig
import time

def check_write_func():
	voice = ""
	x = True
	def check_write(text):
		if text == "прекратить запись":
			x == False
			return x
		
		if text == "удалить все":
			keyboard.press("ctrl")
			keyboard.send("a")
			keyboard.release("ctrl")
			keyboard.send("backspace")
			jconfig.WORD_MEMORY.clear()
	
		if text == "удалить слово":
			print("zxc")
			count = len(jconfig.WORD_MEMORY[len(jconfig.WORD_MEMORY) - 1]) + 1
			for i in range(count + 1):
				keyboard.send("backspace")

		for i, j in jconfig.COM_LIST_PUNCTUATION_COMMAND.items():	
			if i in text:
				x = True
				return x, j, i

			else:
				x = True
		return x		
	
	while x == True:
		print("запись продолжается")

		qwerty = input()
		
		time.sleep(2)

		output = check_write(qwerty)
		if type(output) == bool:
			x = output
			jconfig.WORD_COMMAND[2] = 0
		else:
			qwerty.replace(output[2], "")
			x = output[0]
			jconfig.WORD_COMMAND[1] = output[1]
			jconfig.WORD_COMMAND[2] = output[2]
			if jconfig.WORD_COMMAND[1] == "enter":
				qwerty.replace("enter", "")
			print(qwerty)
		if not qwerty.split():
			pass
		
		else:
			for i in qwerty.split():	
				jconfig.WORD_MEMORY.append(i)

			if jconfig.WORD_COMMAND[1] == 0 and jconfig.WORD_COMMAND[0] != 1:
				print("d")
				keyboard.write(qwerty + " ")

			else:

				if jconfig.WORD_COMMAND[0] == 1:
					print("a")

					if jconfig.WORD_COMMAND[2] != 0:
						print(jconfig.WORD_COMMAND)
						
						if jconfig.WORD_COMMAND[1] == "enter":
							keyboard.write((qwerty.replace(jconfig.WORD_COMMAND[2], "").replace(qwerty[0], qwerty[0].title()) + " "))
							jconfig.WORD_COMMAND[0] = 1
						
						else:
							keyboard.write((qwerty.replace(jconfig.WORD_COMMAND[2], "").replace(qwerty[0], qwerty[0].title()) + " ") + jconfig.WORD_COMMAND[1])	
							jconfig.WORD_COMMAND[0] = 1	

					else:
						try:	
							keyboard.write(qwerty.replace(jconfig.WORD_COMMAND[2], "").replace(qwerty[0], qwerty[0].title()))
						except:
							keyboard.write(qwerty.replace(qwerty[0], qwerty[0].title()))
						jconfig.WORD_COMMAND[1] = 0
						jconfig.WORD_COMMAND[0] = 0
		
				elif jconfig.WORD_COMMAND[1] != 0:
					print("s")
					
					if jconfig.WORD_COMMAND[1] == "enter":
						keyboard.write(qwerty.replace(jconfig.WORD_COMMAND[2], ""))
						jconfig.WORD_COMMAND[0] = 1
					
					else:
						keyboard.write(qwerty.replace(jconfig.WORD_COMMAND[2], "") + jconfig.WORD_COMMAND[1])
						jconfig.WORD_COMMAND[0] = 1
			
			print(jconfig.WORD_COMMAND)
			try:	
				if jconfig.WORD_COMMAND[1] == "enter":
					keyboard.send("enter")
			except:
				pass
		print(jconfig.WORD_MEMORY)
