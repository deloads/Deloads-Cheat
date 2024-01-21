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

class switch:
    def __init__(self,parent,switch_text,func):
        self.func = func
        self.switch = ctk.CTkSwitch(parent,text=switch_text,command=self.toggle)
        self.value = False

    def toggle(self):
        self.value = invert(self.value)
        self.func(self.value)

    def hide(self):
        self.switch.pack_forget()
    
    def show(self):
        self.switch.pack(fill=ctk.X)

class textbox:
    def __init__(self,parent,text):
        self.textbox = ctk.CTkTextbox(parent)
        self.textbox.insert("0.0",text)
        self.textbox.configure(state=ctk.DISABLED)
    
    def hide(self):
        self.textbox.pack_forget()
    
    def show(self):
        self.textbox.pack(fill=ctk.X)

class slider:
    def __init__(self,t,parent,Range,slider_text,value):
        self.value = round(value,3)
        self.text = slider_text
        self.label = t.new_label(f"{self.text}: {round(value,3)}")
        if len(Range) == 3:
            self.slider = ctk.CTkSlider(parent,from_=Range[0],to=Range[1],number_of_steps=Range[2],command=self.slide,variable=ctk.DoubleVar(value=value))
        else:
            self.slider = ctk.CTkSlider(parent,from_=Range[0],to=Range[1],command=self.slide,variable=ctk.DoubleVar(value=value))

    def slide(self,value):
        self.value = round(value,3)
        self.label.label.configure(text=f"{self.text}: {self.value}")

    def hide(self):
        self.slider.pack_forget()
    
    def show(self):
        self.slider.pack(fill=ctk.X)


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
    
    def new_switch(self,switch_text,func):
        s = switch(self.window.right_frame,switch_text,func)
        self.content.append(s)
        return s
    
    def new_textbox(self,text):
        t = textbox(self.window.right_frame,text)
        self.content.append(t)
        return t
    
    def new_slider(self,slider_text,Range,value):
        s = slider(self,self.window.right_frame,Range,slider_text,value)
        self.content.append(s)
        return s