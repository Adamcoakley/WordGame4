from ._anvil_designer import Form4Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from ..Form2 import listOfErrors

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  print(listOfErrors)
  def errors_show(self, **event_args):
    self.errors.text = '\n'.join(listOfErrors)

  def button_1_click(self, **event_args):
    open_form('Form2')

  def button_2_click(self, **event_args):
    open_form('Form1')












