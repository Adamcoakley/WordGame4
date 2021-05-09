from ._anvil_designer import Form3Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import datetime
from datetime import time
from ..Form1 import startTime
from ..Form2 import endTime
from ..Form2 import word_list
from ..Form2 import randomWord


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
  
  def seconds_show(self, **event_args):
    global result
    result = endTime - startTime
    result = result.seconds
    self.seconds.text = result


  def button_1_click(self, **event_args):
    player = self.name.text
    row = app_tables.players.add_row(seconds=result,
                                     name=player,
                                     sourceword=randomWord,
                                     matches=word_list)
    open_form('Form5')

