from tkinter import *
from tkinter import ttk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#6fabc2')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=450)

    def frames_da_tela(self):
        # place, pack, grid
        self.frame1 = Frame(self.root, bd=4, bg='#d0e0f5', 
                            highlightbackground='#022b3a', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#d0e0f5', 
                            highlightbackground='#022b3a', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame1, text="Limpar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_limpar = Button(self.frame1, text="Buscar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white")
        self.bt_limpar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15, )
        ### Criação do botão novo
        self.bt_limpar = Button(self.frame1, text="Novo", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white")
        self.bt_limpar.place(relx=0.58, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_limpar = Button(self.frame1, text="Alterar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white")
        self.bt_limpar.place(relx=0.69, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_limpar = Button(self.frame1, text="Apagar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white")
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criando da label e entrada do codigo
        self.lb_codigo = Label(self.frame1, text="Código", background='#d0e0f5', fg="black")
        self.lb_codigo.place(relx=0.05, rely=0.04)

        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.05, rely=0.14, relwidth=0.13)

        ### Criando da label e entrada do nome
        self.lb_nome = Label(self.frame1, text="Nome", background='#d0e0f5')
        self.lb_nome.place(relx=0.05, rely=0.3)

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.4, relwidth=0.85)

        ### Criando da label e entrada do telefone
        self.lb_telefone = Label(self.frame1, text="Telefone", background='#d0e0f5')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        ### Criando da label e entrada do cidade
        self.lb_cidade = Label(self.frame1, text="Cidade", background='#d0e0f5')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=25, minwidth=25)
        self.listaCli.column("#1", width=75, minwidth=75)
        self.listaCli.column("#2", width=200, minwidth=200)
        self.listaCli.column("#3", width=125, minwidth=125)
        self.listaCli.column("#4", width=125, minwidth=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)

Application()