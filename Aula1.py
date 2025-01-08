from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botões()
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

    def criando_botões(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_limpar = Button(self.frame1, text="Buscar")
        self.bt_limpar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão novo
        self.bt_limpar = Button(self.frame1, text="Novo")
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_limpar = Button(self.frame1, text="Alterar")
        self.bt_limpar.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_limpar = Button(self.frame1, text="Apagar")
        self.bt_limpar.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.15)
    
Application()