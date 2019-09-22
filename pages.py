# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 06:45:37 2019

@author: akris
"""

import urllib.request
from bs4 import BeautifulSoup
from string import ascii_lowercase

for i in ascii_lowercase:
        
    webURL = "https://www.merriam-webster.com/browse/dictionary/"+i+"/1"
    
    page = urllib.request.urlopen(webURL)
    
    soup = BeautifulSoup(page, 'html.parser')
    
    s1 = soup.find('span',class_='counters')
    
    print(i," - ",s1.find(text=True))
    
    