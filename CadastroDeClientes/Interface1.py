from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate
from reportlab import *
import webbrowser
from PIL import *

# Importar as cores
cor1 = '#2F4F4F'  # Bg
cor2 = '#B0C4DE'  # Frames
cor3 = '#20B2AA'  # Botoes
cor4 = '#F8F8FF'  # Branc
cor5 = '#00000'  # Preto

root = Tk()

class Validadores:
    def validate_entry2(self, text):
        if text == "": return True
        try:
            value = int (text)
        except ValueError:
            return False
        return 0 <= value <=1000000



class GradientFrame(Canvas):
    def __init__(self, parent, color1= cor1, color2 = cor2, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color= color1
        self._color2= color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event= None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(r1 + (g_ratio * i))
            nb = int(r1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")

    def gerarelatoriocliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Codigo: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ')
        self.c.drawString(50, 600, 'Cidade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 630, self.telefoneRel)
        self.c.drawString(150, 600, self.cidadeRel)

        self.c.rect(20, 590, 550, 130, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()


class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montaTabelas(self):
        self.conecta_bd();
        print("Conectando ao Banco de Dados")
        # criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                 cod INTEGER PRIMARY KEY,
                 nome_cliente CHAR(40) NOT NULL,
                 telefone INTEGER(20),
                 cidade CHAR(40)
            );
        """)
        self.conn.commit();
        print("Banco de dados Criado")
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_client(self):
        self.variaveis()
        if self.nome_entry.get() == "":
            msg ="Preencha todos os campos!"
            messagebox.showinfo("Cadastro de clieintes - Aviso!", msg)
        else:
            self.conecta_bd()
            self.cursor.execute(""" INSERT INTO clientes (nome_cliente,telefone, cidade)
                 VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
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
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? 
            WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela()
        self.desconecta_bd()

        self.desconecta_bd()


class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg=cor1)
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=500)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg=cor2,
                             highlightbackground=cor4, highlightthickness=2.6)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg=cor2,
                             highlightbackground=cor4, highlightthickness=2.6)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def criando_botoes(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = GradientFrame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background=cor2)
        self.aba2.configure(background="lightgray")

        ##Drop Down Button
        self.Tipvar = StringVar(self.aba2)
        self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
        self.Tipvar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx= 0.1, rely= 0.1, relwidth= 0.2, relheight=0.2)
        self.estado_civil =  self.Tipvar.get()
        print(self.estado_civil)

        self.abas.add(self.aba1, text= "aba 1")
        self.abas.add(self.aba2, text= "aba 2")
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.canvas_bt = Canvas(self.aba1, bd=0, bg=cor2, highlightbackground=cor2 , highlightthickness=2.6)
        self.canvas_bt.place(relx=0.20, rely=0.09, relwidth=0.22, relheight=0.17)

        self.bt_limpar = Button(self.aba1, text="Limpar", bd=2.5, bg=cor1, fg='white', activebackground=cor2,
                                activeforeground="black", font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15, )
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2.5, bg=cor1, fg='white', font=('verdana', 8, 'bold'),
                                command=self.busca_cliente)
        self.bt_buscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo = Button(self.aba1, text="Novo", bd=2.5, bg=cor1, fg='white', font=('verdana', 8, 'bold'),
                              command=self.add_client)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=2.5, bg=cor1, fg='white', font=('verdana', 8, 'bold'),
                                 command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=2.5, bg=cor1, fg='white', font=('verdana', 8, 'bold'),
                                command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novajanela = Button(self.aba1, text="Nova Janela", bd=2.5, bg=cor1, fg='white', font=('verdana', 8, 'bold'),
                                command=self.janela2)
        self.bt_novajanela.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.15)






        self.lb_codigo = Label(self.aba1, text="Código", bg=cor2, fg=cor1, font=('verdana', 9, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.aba1, validate= "key", validatecommand= self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.aba1, text="Nome", bg=cor2, fg=cor1, font=('verdana', 9, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.7)

        self.lb_telefone = Label(self.aba1, text="Telefone", bg=cor2, fg=cor1, font=('verdana', 8, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        self.lb_cidade = Label(self.aba1, text="Cidade", bg=cor2, fg=cor1, font=('verdana', 8, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatorios", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu2.add_command(label="Limpa Cliente", command=self.limpa_tela)

        filemenu2.add_command(label="Ficha do Cliente", command=self.gerarelatoriocliente)
    def janela2(self):
        self.root2 = Toplevel()
        self.root.title("Janela 2")
        self.root2.configure(background=cor2)
        self.root2.geometry("400x200")
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2),"%P")

Application()
