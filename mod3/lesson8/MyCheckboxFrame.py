from customtkinter import *

class MyCheckboxFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure([i for i in range(len(values)+1)], weight=1)

        self.checboxes = []
        
        self.title = CTkLabel(self, text=title, fg_color="blue", corner_radius=10)
        self.title.grid(row=0, column=0, sticky="nsew")
        
        for i,j in enumerate(values):
            self.checboxes.append(CTkCheckBox(self, text=j))
            self.checboxes[i].grid(row=i+1, column=0, sticky="nsew")

    def get(self):
        checked = []
        for i in self.checboxes:
            if i.get()==1:
                checked.append(i.cget("text"))
        return ', '.join(checked)