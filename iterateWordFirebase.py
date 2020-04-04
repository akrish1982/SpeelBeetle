# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:03:24 2019

@author: akris
"""

import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd
#import boto3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

with open('allWordList-a-h1.csv', encoding='utf-8') as csv_file:
    df_wordList = pd.read_csv(csv_file, encoding='utf-8')
    print("read file")
    forms = []
    def1a = []
    #pron = []
    ex = []
    sd = []
    cred = credentials.Certificate('spell-beetle-firebase-adminsdk-v839n-52ddd9da93.json')
    #firebase_admin.initialize_app(cred)
    for index, row in df_wordList.iterrows():
        word = row[1]
        print(word)
        time.sleep(3) #pause the code for 3 seconds            
        webURL = "https://www.merriam-webster.com" + urllib.parse.quote(row[2])            
        print(webURL)
        page = urllib.request.urlopen(webURL)
        
        soup = BeautifulSoup(page, 'html.parser')
        
        s1 = soup.find('h1',class_='hword')
        
        wordForm = s1.find_next('a',class_='important-blue-link')
        try:
            wordForm = wordForm.find_next(text=True)
        except AttributeError:
            wordForm = ""
        forms.append(wordForm)
        
        #pronunciation = s1.find_next('span',class_='pr')
        #try:
        #    pronunciation = pronunciation.find_next(text=True)
        #except AttributeError:
        #    pronunciation = ""
        #pron.append(pronunciation)
        
        
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
        
        
        
        #
        #data = {
        #        u'word': word,
        #            u'wordform': forms,
        #        u'Def1a': def1a
        #        }

        #db.collection(u'data').document(u'one').set(data)
df_wordList['word_form'] = forms
df_wordList['definition'] = def1a
df_wordList['pronunciation'] = sd
df_wordList['Example'] = ex
#print(df_wordList)
df_wordList.drop('Unnamed: 0',axis=1)
#df['Links']=links
#df_wordList.to_csv('allWordList-a-g-out.csv',encoding='utf-8')
#print(df_wordList)

#toJson
d = df_wordList.to_dict('records')

print(d)


for row in d:
    print(row)
    data = firebase_admin.db.reference(url='https://spell-beetle.firebaseio.com')
    wordData = data.child('words').push(value=row)
   

