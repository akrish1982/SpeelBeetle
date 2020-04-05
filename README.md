# SpellBeetle

Python implementation of BeautifulSoup to download all words from the Merriam Websters dictionary. 

The Merriam Websters dictionary is the official dictionary for the Speeling Bee. If you are helping anyone with Spelling Bee, this would be a great resource for you.

PageCount.csv							Write all letters and number of pages in the Merriam Webster.com
allWordList.csv						Downloads each work and links into a csv file
iterateWord.py						Iterate through each word and update Postgres
selectWords.py						Selects words and links from Postgres database
selectWordSounds.py				Selects words and sound files from Postgres database
sounds.py									Download sound files for pronunciation
Words2Postgres.py					Write words and all other information to the Postgres database
iterateWordFirebase.py		Optional iterate each word in csv file and update Firebase database
csvToJSON.py							Optional To change CSV files to JSON
csvtoFirebase.py					Optional to update CSV as a JSON into Google Firebase
firebase conn.py					Optional connect to Firebase
