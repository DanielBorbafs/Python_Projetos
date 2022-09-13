from tkinter import *

from tkinter import ttk
 # Importar as cores
cor1 = '#2F4F4F' # Bg
cor2 = '#B0C4DE' # Frames
cor3 = '#20B2AA' # Botoes
cor4 = '#F8F8FF' # Branco
cor5 = '#00000' # Preto

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg= cor1)
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width= 600, height=500)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg=cor2,
                             highlightbackground=cor4, highlightthickness=2.6)
        self.frame_1.place(relx= 0.02 , rely= 0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg=cor2,
                             highlightbackground=cor4, highlightthickness=2.6)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def criando_botoes(self):
        self.bt_limpar= Button(self.frame_1, text="Limpar", bd=2.5, bg=cor1, fg='white', font=('verdana',8, 'bold'))
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15,)
        self.bt_limpar = Button(self.frame_1, text="Buscar", bd=2.5, bg=cor1, fg='white', font=('verdana',8, 'bold'))
        self.bt_limpar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_limpar = Button(self.frame_1, text="Novo", bd=2.5, bg=cor1, fg='white', font=('verdana',8, 'bold'))
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_limpar = Button(self.frame_1, text="Alterar",bd=2.5, bg=cor1, fg='white', font=('verdana',8, 'bold'))
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_limpar = Button(self.frame_1, text="Apagar", bd=2.5, bg=cor1, fg='white', font=('verdana',8, 'bold'))
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lb_codigo = Label(self.frame_1, text = "Código", bg=cor2, fg=cor1, font=('verdana', 9 , 'bold'))
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome= Label(self.frame_1, text="Nome", bg=cor2, fg=cor1, font=('verdana', 9, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.7)

        self.lb_telefone = Label(self.frame_1, text="Telefone", bg=cor2, fg=cor1, font=('verdana',8, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)


        self.lb_cidade= Label(self.frame_1, text="Cidade", bg=cor2, fg=cor1, font=('verdana',8, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=("col1", "col2", "col3", "col4"))
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
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight= 0.85)
Application()
