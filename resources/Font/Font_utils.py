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

class label:
    def __init__(self,parent,label_text):
        self.label = ctk.CTkLabel(master=parent,text=label_text,anchor='w')
    
    def hide(self):
        self.label.pack_forget()
    
    def show(self):
        self.label.pack(fill=ctk.X)

class button:
    def __init__(self,parent,button_text,func):
        self.button = ctk.CTkButton(parent, text = button_text,command=func,anchor='w')

    def hide(self):
        self.button.pack_forget()
    
    def show(self):
        self.button.pack(fill=ctk.X)


class tab:
    def __init__(self,parent,window,tab_name):
        self.window = window
        self.tap_name = tab_name
        self.button = ctk.CTkButton(parent, text = tab_name,command=self.pressed,anchor='w').pack(fill=ctk.X)
        self.content = []

    def hide_content(self):
        for item in self.content:
            item.hide()
    
    def show_content(self):
        for item in self.content:
            item.show()

    def pressed(self):
        self.window.opentab(self)

    def new_label(self,label_text):
        l = label(self.window.right_frame,label_text)
        self.content.append(l)
        return l
    
    def new_button(self,button_text,func):
        b = button(self.window.right_frame,button_text,func)
        self.content.append(b)
        return b