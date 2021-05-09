import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import random
from collections import Counter

fileWords = app_files.words
fileWords = str(fileWords.get_bytes(), 'utf-8')
fileWords = fileWords.split("\n")
words = {line.strip("\n").replace("'s", "").lower() for line in fileWords}  # A set.
words = sorted(words)[1:]
  
# Filtering the words: created a list to hold words with 8 or more letters.
listValidWords = []
for word in words:
  if len(word) >= 8:
    listValidWords.append(word) 

# Function to generate a random word
@anvil.server.callable
def getRandomWord():
  randomWord = random.choice(listValidWords)
  return randomWord

# Check the number of words
@anvil.server.callable
def checkNumOfWords(word_list):
  numberOfWords = len(word_list)
  return numberOfWords

# Check the words are in the dictionary
@anvil.server.callable
def checkWordsInDictionary(word_list):
  wordsNotInDictionary = []
  for word in word_list:
    if word not in words:
      wordsNotInDictionary.append(word)
  return wordsNotInDictionary

# Check if there are duplicates
@anvil.server.callable
def checkForDupes(word_list):
  nonDuplicates = []
  duplicates = []
  for word in word_list:
    if word not in nonDuplicates:
      nonDuplicates.append(word)
    else:
      duplicates.append(word)
  return duplicates
  
# Check none of the words are the sourceword
@anvil.server.callable
def checkForSourceWord(word_list, randomword):
  for word in word_list:
    if word == randomword:
      return True

# Check the words are all 4+ in length
@anvil.server.callable
def checkEachWord4Letters(word_list):
  wordsLessThanFourLetters = []
  for word in word_list:
    if len(word) < 4:
      wordsLessThanFourLetters.append(word)
  return wordsLessThanFourLetters

# Check if the words are in the source word
@anvil.server.callable
def contains(word_list, randomWord):
  notInSourceWord = []
  for word in word_list:
    chars = list(word)
    for char in chars:
      if char not in randomWord:
        notInSourceWord.append(word)
        break #To prevent the word from adding multiple times a character is not in the word. 
  return notInSourceWord

#/top10 - returns the top 10 scores
##@anvil.server.http_endpoint('/top10')
##def top10Scores(**q):
##    data = []
##    fastestTime = app_tables.players.search(
##    tables.order_by("seconds", ascending=True)
##    )
##    fastestTime = fastestTime[:10]
##    for row in fastestTime:
##      data.append(row['name'])
##      data.append(row['seconds'])
##      data.append(row['sourceword'])
##      data.append(row['matches'])
##    return data



        
  
  
  
  
