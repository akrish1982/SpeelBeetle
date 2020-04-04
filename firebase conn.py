# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:55:57 2020

@author: akris
"""


import firebase_admin
from firebase_admin import credentials

default_app = firebase_admin.initialize_app()

cred = credentials.Certificate("C:\Users\akris\Downloads\spell-beetle-firebase-adminsdk-v839n-013b1c30f0.json")
firebase_admin.initialize_app(cred)
