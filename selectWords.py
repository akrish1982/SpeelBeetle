# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:23:33 2020

@author: akris
"""

import psycopg2
from iterateWordTuple import iterWords

try:
   connection = psycopg2.connect(user="postgres",
                                         password="run4Life",
                                         host="localhost",
                                         port="5432",
                                         database="Dictionary")
   cursor = connection.cursor()
   postgreSQL_select_Query = """select t1.Words,t1.Links from public.Words1 t1 where t1.word_form IS NULL"""

   cursor.execute(postgreSQL_select_Query)

   print("Selecting rows")
   words_records = cursor.fetchall() 
   
   print(words_records)
   iterWords(words_records)

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")