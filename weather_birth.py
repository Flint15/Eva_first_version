import wikipedia
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

config_weather = ["сегодня", "завтра"]

def action(url):
	response = requests.get(url)
	date = []

	soup = BeautifulSoup(response.text, "lxml")

	x = soup.find("tbody").find_all(scope="row", class_="plainlist")

	def bith(qwerty):
		qwerty = qwerty.find(class_="nowrap")
		for i in qwerty:	
			date.append(i.text)
		date.remove(" ")
		return date		
	for i in x:
		if i.text == "Дата рождения":	
			date = bith(i.parent)
	return date 

def person(name):
	wikipedia.set_lang("ru")
	name = wikipedia.page(name).url
	date = action(name)
	return date

def weather(voice):
	url = 'https://www.gismeteo.ru/weather-kolpino-14709/'
	response = requests.get(url, headers={"User-Agent": UserAgent().chrome})   
	soup = BeautifulSoup(response.text, 'lxml')
	
	def detection_day(voice):
		for i in config_weather:
			if i in voice:
				return i

	day = detection_day(voice)	
	
	if day == "сегодня":
		x = soup.find("body").find("div", class_="weathertabs day-1").find("a").find("span", class_="unit unit_temperature_c").text.split()
		print(x[0])
	
	elif day == "завтра":
		x = soup.find("body").find("div", class_="weathertabs day-1").find_all("a")
		
		for i in x:
			if i.get("href") == None:
				pass
			else:
				if "tomorrow" in i.get("href"):
					i = i.find("span", class_="unit unit_temperature_c").text.split()
					print(i[0])
if __name__ == '__main__':
    main()
