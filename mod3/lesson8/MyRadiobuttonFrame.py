from customtkinter import *

class MyRadiobuttonFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure([i for i in range(len(values)+1)], weight=1)

        self.figure = StringVar()
        
        self.title = CTkLabel(self, text=title, fg_color="blue", corner_radius=10)
        self.title.grid(row=0, column=0, sticky="nsew")
        
        for i,j in enumerate(values):
            CTkRadioButton(self, text=j, value = j, variable=self.figure).grid(row=i+1, column=0, sticky="nsew")

    def get(self):
        return self.figure.get()