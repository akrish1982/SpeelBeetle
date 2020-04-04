# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 06:27:58 2020

@author: akris
"""



from firebase_admin import db


for row in d:
    print(row)
    data = firebase_admin.db.Reference
    wordData = data.child('words').push(value=row)
 