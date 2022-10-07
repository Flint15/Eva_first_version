#import j2
#import j3
import daa
import jconfig
import os
import time
import pygame
import keyboard
import datetime
import pyautogui
import webbrowser
from random import randint
from fuzzywuzzy import fuzz
from youtubesearchpython import VideosSearch

voice = ""
def recognition():
	try:	
		qwerty = (j2.va_listen(voice)) 
	except:
		qwerty = ""
	if qwerty == "" or qwerty ==  None:
		qwerty = input()	
	return qwerty

def func_detect(voice):

	def func_detect_com_list(voice):
		test = {"word": "", "percent": 0, "voice": ""}
		test["voice"] = voice
		for i, j in jconfig.COM_LIST.items():
			for x in j:
				sim = fuzz.ratio(voice,x)
				if sim > test["percent"] and x in voice and x == voice:
					test["word"] = i
					test["percent"] = sim
				if x == jconfig.COMMAND_TIME[3]:
					test["word"] = i
					test["percent"] = sim
					test["voice"] = "complite"

		for i, j in jconfig.COM_LIST_WIN_R_COMMAND.items():
			sim = fuzz.ratio(voice,j)
			try:
				if sim > test["percent"] and j in voice and voice.startswith("открой"):
					test["word"] = i
					test["percent"] = sim
					jconfig.COMMAND[0] = test["word"]
					jconfig.COMMAND[2] = "win_r_command"

				if j == jconfig.COMMAND_TIME[3]:
					test["word"] = i
					test["percent"] = sim
					test["voice"] = "complite"
					jconfig.COMMAND[0] = test["word"]
					jconfig.COMMAND[2] = "win_r_command"				
			except:
				pass
		for i, j in jconfig.COM_LIST_WORD.items():
			sim = fuzz.ratio(voice,j)
			
			def check_word_command(voice):
				for i in jconfig.COM_LIST["word"]:
					if i in voice:
						jconfig.COMMAND[1] = "yes"
					else:
						jconfig.COMMAND[1] = "no"
			check_word_command(voice)

			if sim > test["percent"] and jconfig.COMMAND[1] == "yes":
				test["word"] = i
				test["percent"] = sim
				jconfig.COMMAND[0] = test["word"]
				jconfig.COMMAND[2] = "word"
		return test				
	
	qwerty = func_detect_com_list(voice)
	if qwerty["word"] == "open_website":
		def url(voice):	
			test = {"word": "", "percent": 0, "url": ""}
			test["word"] = "open_website"
			for i, j in jconfig.URL_OPEN_WEBSITE.items():
				sim = fuzz.ratio(qwerty["voice"],j)
				if sim > test["percent"]:
					test["url"] = i
					test["percent"] = sim
			return test		
		qwerty = url(qwerty)
	if voice.startswith("выполни") and "через" in voice:
		voice = voice.replace("выполни", "")
		voice = voice.replace("через", "")
		voice = voice.replace("секунд", "")
		voice = voice.split()
		jconfig.COMMAND_TIME[0] = voice[0]
		jconfig.COMMAND_TIME[1] = int(voice[1])
		jconfig.COMMAND_TIME[2] = time.time()

	return qwerty

def auto_func(qwerty):
	def func_reminder(query):

		for i in jconfig.COM_LIST["reminder"]:
			query = query.replace(i, "")
		if ":" in query:
			query = query.replace(":", "")
		if len(query) == 3:
			x = query[0]
			y = str(query[1]) + str(query[2])
		elif len(query) == 4:
			x = str(query[0]) + str(query[1])
			y = str(query[2]) + str(query[3])
	
		deadline = datetime.datetime(2022,7,28,int(x),int(y))
		jconfig.REMINDER.append(deadline)
		
		return deadline
	def call_reminder(deadline):
		now = datetime.datetime.now()
		
		if jconfig.REMINDER[1] > now:
			print(f'{jconfig.REMINDER[1]} не скоро',{now})
		else:
			print("deadline")
			jconfig.REMINDER[0] = "off"
		
		return None
	
	def func_timer():
		if time.time() - jconfig.TIMER[1] >= jconfig.TIMER[2]:
			print("таймер")
			jconfig.TIMER[0] = "off"
		else:
			print("таймер ещё идёт")

	def func_command_time():
		if time.time() - jconfig.COMMAND_TIME[2] >= jconfig.COMMAND_TIME[1]:
			jconfig.COMMAND_TIME = [0, 0, 0, jconfig.COMMAND_TIME[0]]

	if qwerty[0] == "reminder":
		call_reminder(func_reminder(qwerty[1]))
	elif qwerty[0] == "None_reminder":
		call_reminder(jconfig.REMINDER)
	elif qwerty[0] == "timer":
		jconfig.TIMER.append(time.time())
		x = int(qwerty[1])
		x *= 60
		jconfig.TIMER.append(x)
		func_timer()
	elif qwerty[0] == "None_timer":
		func_timer()
	elif qwerty[0] == "COMMAND_TIME0":
		func_command_time()
	elif qwerty == "No":
		return

def auto_action(qwerty):
	if qwerty["word"] == "reminder":
		print("На какое время ?")
		query = recognition()
		jconfig.REMINDER[0] = "on_reminder"
		return qwerty["word"], query
	
	elif qwerty["word"] == "timer":
		print("На какое время ?")
		query = recognition()
		jconfig.TIMER[0] = "on_timer"
		return qwerty["word"], query

	elif jconfig.COMMAND_TIME[0] != 0:
		print("qwerty")
		return "COMMAND_TIME0", "COMMAND_TIME1"

	else:
		if jconfig.REMINDER[0] == "on_reminder":
			return "None_reminder", "None"
		elif jconfig.TIMER[0] == "on_timer":
			return "None_timer", "None"
		elif jconfig.REMINDER[0] == "off":
			return "No"	
		elif jconfig.TIMER[0] == "off":
			return "No"		
		else:	
			return "No"

def run_win_r_command(mix_keys):
	keyboard.send("win+r")
	time.sleep(0.05)
	keyboard.write(mix_keys["word"])
	keyboard.send("enter")
	jconfig.COMMAND = ["q", "q", "q"]

def run_word_command(mix_keys):
	print(mix_keys)
	time.sleep(10)
	keyboard.send(mix_keys)
	jconfig.COMMAND[0] = "q"
	jconfig.COMMAND[1] = "q"
	jconfig.COMMAND[2] = "q"

def func_video(qwerty):
	qwerty = qwerty.replace("открой", "")
	qwerty = qwerty.replace("видио", "")
	qwerty = qwerty.replace("ютубе", "")
	qwerty = qwerty.replace(" в ", "")
	qwerty = qwerty.replace(" ", "")
	videosSearch = VideosSearch(qwerty, limit = 2)
	a = (videosSearch.result())
	url = a["result"][0]["link"]
	webbrowser.open_new(url)

def open_website(url):
	webbrowser.open_new(url)

def write_word():
	voice = ""
	x = True
	def check_write(text):
		if "прекратить запись" in text:
			print(text)
			x = False
		else:
			x = True
		return x	
	while x == True:
		print("запись продолжается")
		qwerty = j2.va_listen(voice)
		keyboard.write(qwerty + " ")
		x = check_write(qwerty)
	print("zx")

def music(voice):
	def func_music():   
		pygame.init()
		song = pygame.mixer.Sound('DVRST Your_Name.mp3')
		clock = pygame.time.Clock()
		return song	
	song = func_music()

	if voice == "выключи музыку":
		song.stop()
		pygame.quit()
	elif voice == "музыка":
		song.play()
	
def random():
	print(randint(0, 1000))

def close_proggarm(voice):
	for i in jconfig.COM_LIST["close_proggram"]:
		voice.replace(i, "")
	voice.replace(" ", "")
	print(voice)
	test = {"word": "", "percent": 0}
	for i, j in jconfig.COMMAND_CLOSE.items():
		for x in j:
			sim = fuzz.ratio(voice, j)
			if sim > test["percent"] and j in voice:
				test["word"] = i
				test["percent"] = sim
	print(test["word"])
	keyboard.send("win+r")
	time.sleep(0.1)
	keyboard.write("cmd")
	time.sleep(0.1)
	keyboard.send("enter")
	time.sleep(0.5)
	keyboard.write("taskkill /f /im " + test["word"] + ".exe")
	keyboard.send("enter")

def OS_command(voice):
	if "перезагрузи" in voice:
		os.system("/REBOOT")
	elif "выключи" in voice:
		os.system("shutdown /s")
	elif "сверн" in voice:
		keyboard.send("win+d")
	elif "экран блокировки":
		print("12")
		keyboard.press("win")
		keyboard.send("l")	

def open_proggram_func(voice):
	if "телеграм" in voice:
		keyboard.send("win")
		time.sleep(0.5)
		keyboard.write("telegram")
		time.sleep(0.5)
		keyboard.send("enter")
	elif "дискорд" in voice:
		keyboard.send("win")
		time.sleep(0.5)
		keyboard.write("discord")	
		time.sleep(0.5)
		keyboard.send("enter")
	if "спотифай" in voice:
		keyboard.send("win")
		time.sleep(0.5)
		keyboard.write("spotify")	
		time.sleep(0.5)
		keyboard.send("enter")
	if "стим" in voice:
		keyboard.send("win")
		time.sleep(0.5)
		keyboard.write("steam")	
		time.sleep(0.5)
		keyboard.send("enter")

def action(qwerty):
	if qwerty["word"] == "say":
		j3.va_speak("Здраствуйте сэр")
	if qwerty["word"] == "open_file":
		os.system("zx.txt")
	if qwerty["word"] == "open_browser":
		webbrowser.open("opera")
	if qwerty["word"] == "time":
		print(datetime.datetime.now())
	if qwerty["word"] == "date_bith":
		print("Кто ?")
		name = recognition()
		print(" ".join(daa.person(name)))
	if qwerty["word"] == "open_youtube":
		func_video(qwerty["voice"])
	if qwerty["word"] in jconfig.COMMAND and jconfig.COMMAND[2] == "win_r_command":
		print(qwerty["word"])
		run_win_r_command(qwerty)
	if qwerty["word"] == "open_website":
		open_website(qwerty["url"])
	if jconfig.COMMAND[2] == "word":
		query = ""
		for i in jconfig.COM_LIST["word"]:
			query = qwerty["voice"].replace(i, "")
		print(query)	
		qwerty = func_detect(query)
		run_word_command(jconfig.COMMAND[0])
	if qwerty["word"] == "write_word":
		print("запись идёт")
		time.sleep(6)
		write_word()
	if qwerty["word"] == "weather":
		daa.weather(qwerty["voice"])
	if qwerty["word"] == "music":
		music(qwerty["voice"])
	if qwerty["word"] == "OS_command":
		OS_command(qwerty["voice"])
	if qwerty["word"] == "random" or jconfig.COMMAND_TIME[3] == "рандом":
		random()
	if qwerty["word"] == "close_proggram":
		close_proggarm(qwerty["voice"])
	if qwerty["word"] == "change_language":
		keyboard.send("shift+alt")
	if qwerty["word"] == "open_proggram":
		open_proggram_func(qwerty["voice"])

	if qwerty["voice"] == "complite":
		jconfig.COMMAND_TIME = [0, 0, 0, 0]

	return None
# Проверку можно сделать с помощью for где i будет каждая комманда/ключ из COM_LIST
# Так можно будет оптимизировать проверку

def va_respond(voice: str):

    print(voice)
    voice.replace(jconfig.NAME, "")
    qwerty = func_detect(voice)
    auto_func(auto_action(qwerty))
    action(qwerty)
    return

while True:

	qwerty = recognition()
	if qwerty == "":
		pass
	else:
		va_respond(qwerty)