# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:03:24 2019

@author: akris
"""

import urllib.request
from bs4 import BeautifulSoup
import time
from Words2Postgres import updateInBulk

#tuple

def iterWords(wordrows):
    rnum=0
    wordTupTuple = []
    for row in wordrows:

        word = row[0]
        print(word)
        time.sleep(0.04) #pause the code for 1 seconds            
        webURL = "https://www.merriam-webster.com" + urllib.parse.quote(row[1])            
        #print(webURL)
        try:
            page = urllib.request.urlopen(webURL)
            soup = BeautifulSoup(page, 'html.parser')
        
            s1 = soup.find('h1',class_='hword')
            
            wordForm = s1.find_next('a',class_='important-blue-link')
            try:
                wordForm = wordForm.find_next(text=True)
            except AttributeError:
                wordForm = ""
            #forms.append(wordForm)
            
            definition = s1.find_next('span',class_='dtText')
            try:
                definition = definition.get_text()
            except AttributeError:
                definition = ""
            #def1a.append(definition)
            
            #Sound
            sound = s1.find_next('span',class_='prs')
            
            try:
                sound = sound.find_next('a',class_='play-pron hw-play-pron')
                #print(sound)
                soundStr = str(sound.get('data-dir')) +'/' + str(sound.get('data-file'))
                #print(soundStr)
            except AttributeError:
                soundStr = ""
            #sd.append(soundStr)
            
            #Example
            s1 = soup.find('span',class_='t has-aq')
            try:
                example = s1.get_text()
                #print(example)
            except AttributeError:
                example = ""
            #ex.append(example)
            
            
            try:
                s1 = soup.find('p',class_='et')
                #print(s1)
                etymology = s1.get_text().strip()
            except AttributeError:
                etymology = ""
            #print(etymology)
            #et.append(etymology)
            wordTup = (wordForm,definition,soundStr,example,etymology,word)
            wordTupTuple.append(wordTup)
            #print(rnum)
            
            if rnum > 1:
                 print("Update ",word)
                 updateInBulk(wordTupTuple)
                 wordTupTuple.clear()
                 rnum = 0
            else:
                rnum = rnum + 1
           
        except:
            print(Exception)
    
            

        
