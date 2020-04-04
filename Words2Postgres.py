# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:51:17 2020

@author: akris
"""

#Update Postgres

import psycopg2

def updateInBulk(records):
    try:
        ps_connection = psycopg2.connect(user="postgres",
                                         password="run4Life",
                                         host="localhost",
                                         port="5432",
                                         database="Dictionary")
        cursor = ps_connection.cursor()

        # Update multiple records
        sql_update_query = """Update public.Words1 set word_form = %s, definition = %s,pronunciation = %s,Example= %s
                             ,etymology= %s where Words = %s"""
        cursor.executemany(sql_update_query, records)
        ps_connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")