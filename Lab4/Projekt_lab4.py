# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:58:20 2021

@author: weron
"""
import json
import argparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

parser = argparse.ArgumentParser(description = "Opis")
parser.add_argument('-file', help = 'file name', type = str, default = 'Ciasta')
args = parser.parse_args()

data = []

options = Options()
options.add_argument('--disable-notifications')

service = Service('chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)           #wyłącza notyfikacje
driver.get('https://www.domowe-wypieki.pl/')

#włączenie zgody
button = driver.find_element(By.XPATH, '//*[@id="sunfw-master"]/div[1]/div[2]/a')    
button.click()
time.sleep(1)

#przewijanie
for i in range(10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

#wczytanie w konsole
elements = driver.find_elements(By.CSS_SELECTOR, 'span')

for element in elements:
    print(element.text)
    data.append(element.text)

with open(f'{args.file}.json', "w", encoding = "utf-8") as f:
    json.dump(data, f)
   
driver.close()