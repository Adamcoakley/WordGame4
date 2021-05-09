from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import datetime
from datetime import time
## from collections import Counter


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global randomWord
    randomWord = anvil.server.call('getRandomWord')
    self.sourceword.text = randomWord
    
    global listOfErrors
    listOfErrors = [] # Will append this after each check.
    
  def button_1_click(self, **event_args):
    global endTime
    endTime = datetime.datetime.now()
    allWords = self.text_box.text
    global word_list
    word_list = allWords.split()
    for i in range(len(word_list)):
       word_list[i] = word_list[i].lower()
    print(word_list)
    
    """ To check: 
        1. Check that there's the correct number of words (7)
        2. Check all words are 4+ in length
        3. Check the words are in the sourceword
        4. Check the words are in the dictionary
        5. Check there are no duplicates
        6. Check none of the words are the sourceword.
     """
    
    #Check1 - Correct number of words
    numberOfWords = anvil.server.call('checkNumOfWords', word_list)
    if numberOfWords != 7:
      error1 = 'You have an incorrect number of words: ' + str(numberOfWords) + ' not 7.'
      listOfErrors.append(error1)
      
    #Check2 - All words are in dictionary
    wordsNotInDictionary = anvil.server.call('checkWordsInDictionary', word_list)
    if len(wordsNotInDictionary) > 0:
      str1 = ""
      for word in wordsNotInDictionary:
        str1 += word + ' '
      error2 = 'You misspelt these words: ' + str1
      listOfErrors.append(error2)
    
    #Check3 - Check each word is 4+ in length
    wordsLessThan4 = anvil.server.call('checkEachWord4Letters', word_list)
    if len(wordsLessThan4) > 0:
      str2 = ""
      for word in wordsLessThan4:
        str2 += word + ' '
      error3 = 'These words are too small: ' + str2
      listOfErrors.append(error3)
    
    #Check4 - Check the sourceword isn't in the list
    inSourceWord = anvil.server.call('checkForSourceWord', word_list, randomWord)
    if inSourceWord == True:
      listOfErrors.append('You used the sourceword.')
    
    #Check5 - Check there are no duplicates
    duplicates = anvil.server.call('checkForDupes', word_list)
    if len(duplicates) > 0:
      str3 = ""
      for word in duplicates:
        str3 += word + ' '
      error4 = "You have duplicates in your list: " + str3
      listOfErrors.append(error4)
      
    #Check6 - Check the words are in the sourceword
    inWord = anvil.server.call('contains', word_list, randomWord)
    if len(inWord) > 0:
      str4 = ""
      for word in inWord:
        str4 += word + ' '
      error5 = "These words are not in the sourceword: " + str4
      listOfErrors.append(error5)
      
    #Winner or loser?
    if len(listOfErrors) > 0:
      open_form('Form4')
    else:
      open_form('Form3')
      
    
 