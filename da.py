import os
import time
import datetime
import requests
import pyglet
import json
#import pygame
from bs4 import BeautifulSoup
import jconfig
#import j2
#import j3
import subprocess
import keyboard
from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
voice = ""
import requests
from fake_useragent import UserAgent
import smtplib


"""def s():
   driver = webdriver.Chrome()
   try:
      driver.get("https://www.youtube.com/results?search_query=ai")
      time.sleep(40)

      with open("ind.html", "w") as file:
         file.write(driver.page_source)

   except Exception as ex:
      print(ex)
   finally:
      driver.close()
      driver.quit()   
#s()"""


"""   url = 'https://www.gismeteo.ru/weather-kolpino-14709/'
   
      response = requests.get(url, headers={"User-Agent": UserAgent().chrome})   
      
      soup = BeautifulSoup(response.text, 'lxml')
      
      x = soup.find("body").find("div", class_="weathertabs day-1").find("a").find("span", class_="unit unit_temperature_c").text.split()

#for key, value in response.request.headers.items():
#    print(key+": "+value)
from youtubesearchpython import VideosSearch

#videosSearch = VideosSearch('шевцова', limit = 5)
#a = (videosSearch.result())

from selenium import webdriver
from bs4 import BeautifulSoup as BS

URL = "https://www.youtube.com/c/AzzraelCode/videos"

driver = webdriver.Opera()
driver.get(URL)
time.sleep(10)  #Можно ждать до загрузки страницы, но проще подождать 10 секунд, их хватит с запасом
html = driver.page_source

soup = BS(html, "html.parser")
videos = soup.find_all("ytd-grid-video-renderer",{"class":"style-scope ytd-grid-renderer"})
for video in videos:
   a = video.find("a",{"id":"video-title"})
   name = link.get_text()
   link = "https://www.youtube.com/" + a.get("href") 
   print(name, link)

from selenium import webdriver
from selenium.webdriver.chrome import service


driver = webdriver.Opera('D:/Programming/Sublime_text/Project_Sublime/AI/j/operadriver')
driver.get('http://google.com')

from fake_useragent import UserAgent
url = "https://www.gismeteo.ru/weather-kolpino-14709/"
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})

soup = BeautifulSoup(response.text,'html.parser') 

print(soup)"""

#driver = webdriver.Chrome()
#driver.get("https://google.com/")
#time.sleep(15)
#x = driver.page_source

"""url = 'https://www.gismeteo.ru/weather-kolpino-14709/'
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})   
soup = BeautifulSoup(response.text, 'lxml')
soup = str(soup)
q = open("qwerty.txt", "w+")
q.write(soup)"""

#print(datetime.time(minute))
"""url = 'https://lenta.ru'
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})   
soup = BeautifulSoup(response.text, 'lxml')
soup.find("a", class_="_news _topnews bbjq card-big")
print(soup)"""

server = smtplib.SMTP("smpt.gmail.com",587)
server.helo()
