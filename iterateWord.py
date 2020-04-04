# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:03:24 2019

@author: akris
"""

import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd

with open('allWordList-a-h1.csv', encoding='utf-8') as csv_file:
    df_wordList = pd.read_csv(csv_file, encoding='utf-8')
    print("read file")
    forms = []
    def1a = []
    et = []
    ex = []
    sd = []
    
    for index, row in df_wordList.iterrows():
        word = row[1]
        print(word)
        time.sleep(1) #pause the code for 1 seconds            
        webURL = "https://www.merriam-webster.com" + urllib.parse.quote(row[2])            
        print(webURL)
        try:
            page = urllib.request.urlopen(webURL)
            soup = BeautifulSoup(page, 'html.parser')
        
            s1 = soup.find('h1',class_='hword')
            
            wordForm = s1.find_next('a',class_='important-blue-link')
            try:
                wordForm = wordForm.find_next(text=True)
            except AttributeError:
                wordForm = ""
            forms.append(wordForm)
            
            definition = s1.find_next('span',class_='dtText')
            try:
                definition = definition.get_text()
            except AttributeError:
                definition = ""
            def1a.append(definition)
            
            #Sound
            sound = s1.find_next('span',class_='prs')
            
            try:
                sound = sound.find_next('a',class_='play-pron hw-play-pron')
                #print(sound)
                soundStr = str(sound.get('data-dir')) +'/' + str(sound.get('data-file'))
                #print(soundStr)
            except AttributeError:
                soundStr = ""
            sd.append(soundStr)
            
            #Example
            s1 = soup.find('span',class_='t has-aq')
            try:
                example = s1.get_text()
                print(example)
            except AttributeError:
                example = ""
            ex.append(example)
            
            
            try:
                s1 = soup.find('p',class_='et')
                print(s1)
                etymology = s1.get_text().strip()
            except AttributeError:
                etymology = ""
            print(etymology)
            et.append(etymology)
        except:
            break
        
        
        

        
df_wordList['word_form'] = forms
df_wordList['definition'] = def1a
df_wordList['pronunciation'] = sd
df_wordList['Example'] = ex
df_wordList['etymology'] = et

df_wordList.drop('Unnamed: 0',axis=1)
#df['Links']=links
df_wordList.to_csv('allWordList-a-h-out.csv',encoding='utf-8')
