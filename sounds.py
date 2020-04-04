# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:08:45 2020

@author: akris
"""

# download https://media.merriam-webster.com/audio/prons/en/us/mp3/a/act00001.mp3
import urllib.request
import time
import requests

def sounddwnld(wordlist):
        
    for row in wordlist:
        time.sleep(1) #pause the code for 1 seconds            
        url1 = row[1]+'.mp3'
        url = 'https://media.merriam-webster.com/audio/prons/en/us/mp3/'+ urllib.parse.quote(url1)     
        print(url)
        try:
            myfile = requests.get(url)
            name = 'sounds/' + url1
            folder = row[1].split('/')
            print(name, folder[0])
            folder[0] = 'sounds/'+folder[0]
            import os
            if not os.path.exists(folder[0]):
                os.makedirs(folder[0])
            open(name, 'wb').write(myfile.content)    
        except(Exception) as error:
            print(error)
            