# -*- coding: utf-8 -*-
"""
Lis Weronika
Projekt003
Scraping
"""

import json
import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description = "Opis")
parser.add_argument('-file', help = 'file name', type = str, default = 'Filmy')
args = parser.parse_args()

data = []

req = requests.get('https://zalukaj.cc/')

soup = BeautifulSoup(req.text, 'html.parser')
print(soup.title.text)

divs_films = soup.find('div', id = 'tab-1')
divs_films_2 = divs_films.find_all('div', class_ = 'wrapper')

for film in divs_films_2:
    
    title = film.find('h3', class_ = "title")
    title2 = title.find('a').text
    genere = film.find('div', class_ = 'genere')
    viwes = film.find('div', class_ = 'views').text
    version = film.find('div', class_ = 'version')
    version2 = version.find('div', class_ = 'tooltip').text
    
    show = {"TYTUL:": title2, "ROK:": genere, "WIDZIANO:":viwes, "INFO:": version2}
    data.append(show)

with open(f'{args.file}.json', "w", encoding = "utf-8") as f:
    json.dump(data, f)
   
