# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:09:25 2017

@author: pablo
"""

# https://automatetheboringstuff.com/chapter11/
# A much shorter version: 
#https://gist.github.com/bradmontgomery/1872970


# BeautifulSoup docs:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests, bs4
import codecs
import unidecode

##################################################################
### Scrapping Prague's wikipedia
##################################################################
res = requests.get('https://en.wikipedia.org/wiki/Prague')

res.status_code # Status: 200 is ok, 404 is not found

## Parse response with res.text or res.content. "lxml" is the recommended parser
page = bs4.BeautifulSoup(res.content, "lxml")

# Print the page to see that format is correct
page

unis = page.select('#Public_universities')[0].find_next('ul').find_all('li')
                   
for uni in unis:
    print(uni.text)


##################################################################
### Hospodarske noviny: top 10
##################################################################
res = requests.get('http://ihned.cz')

page = bs4.BeautifulSoup(res.content, "lxml") 


# Get all links
for link in page.find_all('a'):
    print(link.get('href'))


# Titles of first page articles
headlines = page.find_all("div", class_="stats-article ga-edl ga-edl-most_read")

type(headlines) #It's a list! so we can iterate
len(headlines)


for h in headlines:
    print('*'*10)
    print(h.find('a')['href']), print(h.text)


# Parse it for something else
urls = ['http:'+h.find('a')['href'] for h in headlines]
urls
desc = [h.find('a').text for h in headlines]
   

# Remove those cute hats
import unidecode
unidecode.unidecode(desc[0])


# Save the data
with codecs.open('demo.csv','w', encoding='utf8') as f:
    for h in zip(urls,desc):
        f.write(h[0]+';'+h[1]+'\n')
f.close()    


### EXERCISE: Can you modify the code to save the urls without diacritics?
## how about including the authors too?
authors = [h.find('a')['data-author'] for h in headlines]


##################################################################
## EXERCISE: Parsing that horrible Cinemacity website
##################################################################
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