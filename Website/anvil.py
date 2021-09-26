from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    predictions = []
    i = 0
    text = self.text_area.text.split()
    
    while i < len(text):
        #calling the spellCheck function and passing the text user entered
        correctedText = anvil.server.call("spellCheck", text[i])
        predictions.append(correctedText)  
        self.label_1.text = predictions
        i += 1      
        