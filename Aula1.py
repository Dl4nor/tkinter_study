from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#6fabc2')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    def frames_da_tela(self):
        # place, pack, grid
        self.frame1 = Frame(self.root, bd=4, bg='#d0e0f5', 
                            highlightbackground='#022b3a', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#d0e0f5', 
                            highlightbackground='#022b3a', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        
        
Application()