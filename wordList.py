# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 04:30:07 2019

@author: akris
"""
import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd

with open('PageCount-test.csv') as csv_file:
    df_pageCount = pd.read_csv(csv_file)
    words = []
    links = []
    for index, row in df_pageCount.iterrows():
        alpha = row[0]
        for page in range(1,row[1]+1):
            time.sleep(3) #pause the code for 3 seconds
            
            webURL = "https://www.merriam-webster.com/browse/dictionary/" + alpha + "/" + str(page)
            
            print(webURL)
            
            page = urllib.request.urlopen(webURL)
            
            soup = BeautifulSoup(page, 'html.parser')
            
            s1 = soup.find('div',class_='entries')
            
            for i in s1.find_all('a'):
                words.append(i.find(text=True))
                links.append(i.get('href'))
df = pd.DataFrame(words,columns=['Words'])
df['Links']=links
df.to_csv('allWordList-u-z.csv')
  

