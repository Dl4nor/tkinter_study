from tkinter import *
from tkinter import ttk
import sqlite3
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = Tk()

class Relatorios():
    def printCliente(self):
        pathRelCli = os.path.abspath("./relatorios/Cliente-"+self.codigoRel+".pdf")
        webbrowser.open(pathRelCli)
    
    def gerarRelatCliente(self):
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        if not os.path.exists("./relatorios"):
            os.makedirs("./relatorios")

        self.c = canvas.Canvas("./relatorios/Cliente-"+self.codigoRel+".pdf")

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 640, 'Telefone: ')
        self.c.drawString(50, 610, 'Cidade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 640, self.foneRel)
        self.c.drawString(150, 610, self.cidadeRel)

        self.c.rect(20, 590, 550, 140, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()

class Functions():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("db_clientes.sqlite")
        self.cursor = self.conn.cursor(); print('Conectando ao banco...')
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do banco...")
    def montaTabelas(self):
        self.conecta_bd()
        ### Criação da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tb_clientes(
                cod             INTEGER PRIMARY KEY,
                nome_cliente    CHAR(40) NOT NULL,
                telefone        CHAR(20),
                cidade          CHAR(40)
            );
        """)
        self.conn.commit()
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()

        self.conecta_bd()

        self.cursor.execute("""
            INSERT INTO tb_clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?);
        """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()

        self.desconecta_bd()

        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        
        self.conecta_bd()

        lista = self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, cidade
            FROM tb_clientes
            ORDER BY nome_cliente ASC;
        """)
        for i in lista:
            self.listaCli.insert("", END, values=i)

        self.desconecta_bd()

    def onDloubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""
            DELETE FROM tb_clientes
            WHERE cod = ?
        """, (self.codigo,))
        self.conn.commit()

        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""
            UPDATE tb_clientes
            SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ?
        """, (self.nome, self.telefone, self.cidade, self.codigo))

        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

class Application(Functions, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
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
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white",
                                command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame1, text="Buscar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white")
        self.bt_buscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15, )
        ### Criação do botão novo
        self.bt_novo = Button(self.frame1, text="Novo", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white",
                                command=self.add_cliente)
        self.bt_novo.place(relx=0.58, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_alterar = Button(self.frame1, text="Alterar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white",
                                command=self.altera_cliente)
        self.bt_alterar.place(relx=0.69, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_apagar = Button(self.frame1, text="Apagar", bd=0.7, bg="#1f7a8c", fg="white",
                                font=('calibri', 11, 'bold'), activebackground="#022b3a", activeforeground="white",
                                command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

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
        self.listaCli.bind("<Double-1>", self.onDloubleClick)

    def Menus(self):
        menubar = Menu(self.root, tearoff=0)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)
        filemenu3 = Menu(menubar, tearoff=0)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Relatórios", menu= filemenu2)
        menubar.add_cascade(label= "Sobre", menu=filemenu3)

        filemenu.add_command(label= "Sair", command= Quit)
        filemenu.add_command(label= "Limpa Cliente", command= self.limpa_tela)

        filemenu2.add_command(label= "Ficha do Cliente", command=self.gerarRelatCliente)

Application()