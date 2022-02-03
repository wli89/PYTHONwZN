import requests
from bs4 import BeautifulSoup
import os
import time
import threading

def pobieranie(adres, kod):
    obrazek = link + '/' + adres
    print(obrazek)
    with open(file_path + '/' + kod + adres, 'wb') as handler:
        handler.write(requests.get(obrazek).content)

file_path = os.path.dirname(os.path.abspath(__file__))
link = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir' 
url = requests.get(link)
soup = BeautifulSoup(url.text,"html.parser")
adresy = []

for a in soup.find_all('a', href=True):
    if a["href"][a["href"].rfind(".")+1:] in ['png']:
        adresy.append(a["href"])
#print(adresy)

t = time.time()
for img in adresy:
    pobieranie(img,'1')
print('Klasyczne: ' + str(time.time()-t))

t = time.time()
threads = []
for img in adresy:
    threads.append(threading.Thread(target=pobieranie, args=(img, '2')))
for p in threads:
    p.start()
for p in threads:
    p.join()
print('Wielow: ' + str(time.time()-t))

