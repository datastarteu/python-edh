# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:42:13 2017

@author: pc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:09:25 2017

@author: pablo
"""

# https://automatetheboringstuff.com/chapter11/


import requests, bs4
import codecs

res = requests.get('http://ihned.cz')

res.status_code # Status: 200 is ok, 404 is not found

page = bs4.BeautifulSoup(res.text, "lxml")

# Titles of first page articles
headlines = page.select(".article-title")

type(headlines) #It's a list! so we can iterate

for h in headlines:
    print('*'*10)
    print(h.find('a')['href']), print(h.text)


# Parse it for something else
urls = [h.find('a')['href'] for h in headlines]
desc = [h.text for h in headlines]
   

# Save the data
with codecs.open('demo.csv','w', encoding='utf8') as f:
    for h in headlines:
        f.write('http:'+h.find('a')['href']+'|'+h.text+'\n')
f.close()    

### SCRAPPING ROHLIK.CSV

res = requests.get('https://www.rohlik.cz/c300103000-maso-a-ryby')
page = bs4.BeautifulSoup(res.text, "lxml")

prods = page.select('.product__right')

for p in prods:
    print("Product name: ", p.select('.product__name')[0].text)

# Mmm... whitespaces
p.select('.product__name')[0].text.strip()    
    

# Here we go again
with codecs.open('prices_rohlik.csv','w', encoding='utf8') as f:
    for p in prods:
        prod = p.select('.product__name')[0].text
        prod = prod.strip()
        price_per_kilo = p.select('.product__price span')[0].text
        f.write(prod+'|'+price_per_kilo+'\n')        
f.close()    


## EXERCISE

res = requests.get("http://cinemacity.cz/scheduleInfo?locationId=1010105&date=null&venueTypeId=0&hideSite=0&openedFromPopup=1")
page = bs4.BeautifulSoup(res.text, "lxml")

movies_table = page.find('table', {'class':"scheduleInfoTable"})
movies_tbody = movies_table.find('tbody')

rows = movies_tbody.find_all('tr')

with codecs.open('movies.csv', 'w',encoding='utf8') as f:
    for row in rows:
        cols = row.find_all('td')
        row = [el.text.strip() for el in cols]
        title = row[0]
        clasif = row[1]
        audio = row[2]
        text = row[3]
        duration = row[4]
        times = [t for t in row[5:] if t != '']
        f.write(title + '|'+clasif+'|'+audio+'|'+text+'|'+duration+'|'+str(times)+'\n')