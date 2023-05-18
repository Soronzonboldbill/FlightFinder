"""
    selenium-learning.py: a quick and dirty program that I use to find out 
    the main functionality of selenium. 

    Purpose: Create a barebones web scraper that looks for 
             for NBA player salaries from the website: 
             https://hoopshype.com/salaries/players/   
    Date   : 5/18/2023 
    Author : Bill Soronzonbold
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
service = Service(executable_path="browserDrivers/chromedriver")

urls = ['https://hoopshype.com/salaries/players/'] 

# boiler plate code to open the website
driver = webdriver.Chrome(service=service, options=options)  
driver.get(urls[0])  

players = driver.find_elements('xpath', '//td[@class="name"]')
players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)

salaries = driver.find_elements('xpath', '//td[@class="hh-salaries-sorted"]') 
salaries_list = []
for s in range(len(salaries)): 
    salaries_list.append(salaries[s].text)

print(salaries_list) 
 

# final piece of boiler plate to close the driver connection 
driver.quit()