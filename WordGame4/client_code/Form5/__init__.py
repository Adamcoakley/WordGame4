from ._anvil_designer import Form5Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..Form3 import result

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    #Number of players
    numOfPlayers = len(app_tables.players.search())
    self.players.text = numOfPlayers 
    #Position
    results = [r['seconds'] for r in app_tables.players.search()]
    results.sort()
    position = results.index(result)
    position = position + 1
    self.position.text = position
    #Sort the list + print first 10
    fastestTime = app_tables.players.search(
      tables.order_by("seconds", ascending=True)
    )
    fastestTime = fastestTime[:10]
    self.repeating_panel_1.items = fastestTime
    
   
  def button_1_click(self, **event_args):
    open_form('Form2')
    

  def button_2_click(self, **event_args):
    open_form('Form1')


