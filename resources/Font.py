import resources.Font_utils as utils
import customtkinter as ctk

class window(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        self.geometry(f"{utils.config['window']['size'][0]}x{utils.config['window']['size'][1]}")
        self.title(utils.config['window']['title'])

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=6)

        #frames
        self.left_frame = utils.frame(self,0)
        self.right_frame = utils.frame(self,1)

        self.tabs = []

    def run(self):
        self.mainloop()

    def hide_content(self):
        for tab in self.tabs:
            tab.hide_content()

    def opentab(self,tab):
        self.hide_content()
        tab.show_content()
    
    def new_tap(self,tab_name):
        tab = utils.tab(self.left_frame,self,tab_name)
        self.tabs.append(tab)
        return tab