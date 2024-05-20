import time
from urllib.parse import quote

import selenium.common.exceptions as Exception
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

with open("message.txt", "r") as file:
    msg = file.read()

msg = quote(msg)

numbers = []
with open("numbers.txt", "r") as file:
    for num in file.readlines():
        numbers.append(num.rstrip())

chrome_version = "93.0.4577.63"  

driver = webdriver.Chrome(service = Service(ChromeDriverManager(version = chrome_version).install()))

link = "https://web.whatsapp.com"

driver.get(link)

time.sleep(30)

for num in numbers:
    link2 = f"https://web.whatsapp.com/send/?phone=91{num}&text={msg}"
    try:
        driver.get(link2)
        time.sleep(20)
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(10)
    except Exception:
        print(num)
time.sleep(18000)
