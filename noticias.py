from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import bs4
import os

print("Abrindo o browser...")

username="saulocatharino@gmail.com"
password="xxxxxxxx"

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities['marionette'] = False

binary = FirefoxBinary(r'/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)
driver.get('https://news.google.com/foryou?hl=pt-BR&gl=BR&ceid=BR%3Apt-419')

driver.find_element_by_id('identifierId').send_keys(username)
driver.find_element_by_id('identifierId').send_keys(chr(13))


time.sleep(2)

driver.find_element_by_class_name('zHQkBf').send_keys(password)
driver.find_element_by_class_name('zHQkBf').send_keys(chr(13))

time.sleep(4)

soup = bs4.BeatifulSoup(driver.page_source, 'lxml')
news = []

for link in soup.select('span')
    if str(link)[0:6] == "<span>"
        news.append(str(link).replace("<span>","").replace("</span>","")
        print(str(link).replace("<span>","").replace("</span>",""))

sounds = []
z = 0

for new in news:
    tts = gTTs(text= new, lang = 'pt')
    print("response" + str(z)+".mp3")
    tts.save("response" + str(z) + ".mp3")
    time.sleep(2)
    os.system("mplayer reponse" + str(z) ".mp3")
    z += 1
