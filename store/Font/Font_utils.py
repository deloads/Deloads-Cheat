import json
import customtkinter as ctk


with open("data/config.json","r") as json_file:
    config =  json.load(json_file)

def invert(data):
    if data == True:
        return False
    if data == False:
        return True

class frame(ctk.CTkScrollableFrame):
    def __init__(self,parent,col):
        super().__init__(master=parent)
        self.grid(row = 0,column = col,sticky=ctk.NSEW,padx=3,pady=3)

class tab:
    def __init__(self,parent,window,tab_name):
        self.window = window
        self.tap_name = tab_name
        self.button = ctk.CTkButton(parent, text = tab_name,command=self.pressed).pack(fill=ctk.X)

    def pressed(self):
        self.window.opentab(self.tap_name)